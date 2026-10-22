"""Solve bounded integer difference constraints and expose a contradictory cycle."""

def analyze(data):
    obj(data,['variables','constraints'])
    vs=sequence(data['variables'],100)
    if not vs: raise ValueError('at least one variable required')
    for v in vs: ident(v)
    if len(set(vs))!=len(vs): raise ValueError('duplicate variable')
    edges=[];ids=set()
    for e in sequence(data['constraints'],1000):
        obj(e,['id','from','to','max']);ident(e['id']);ident(e['from']);ident(e['to']);integer(e['max'])
        if e['id'] in ids or e['from'] not in vs or e['to'] not in vs: raise ValueError('duplicate edge ID or unknown variable')
        ids.add(e['id']);edges.append(dict(e))
    dist={v:0 for v in vs};pred={};changed=None
    for _ in vs:
        changed=None
        for e in edges:
            if dist[e['to']]>dist[e['from']]+e['max']:
                dist[e['to']]=dist[e['from']]+e['max'];pred[e['to']]=e;changed=e['to']
        if changed is None: break
    if changed is None:
        m=min(dist.values());assignment={k:v-m for k,v in dist.items()}
        return {'feasible':True,'assignment':assignment,'slacks':[{'id':e['id'],'slack':e['max']-(assignment[e['to']]-assignment[e['from']])}for e in edges]}
    v=changed
    for _ in vs: v=pred[v]['from']
    start=v;cycle=[]
    while True:
        e=pred[v];cycle.append(e);v=e['from']
        if v==start:break
    cycle.reverse()
    total=sum(e['max']for e in cycle)
    assert total<0 and all(cycle[i]['to']==cycle[(i+1)%len(cycle)]['from']for i in range(len(cycle)))
    return {'feasible':False,'cycle':cycle,'sum_max':total,'contradiction':'Summing these bounds requires 0 <= '+str(total)}
import argparse, json, pathlib, sys

def obj(v, keys, required=None):
    if type(v) is not dict or set(v)-set(keys) or set(required if required is not None else keys)-set(v):
        raise ValueError('invalid object keys: '+str(keys))
    return v

def integer(v, low=-10**12, high=10**12):
    if type(v) is not int or not low<=v<=high: raise ValueError('integer outside supported range')
    return v

def ident(v):
    if type(v) is not str or not 1<=len(v)<=128: raise ValueError('identifier must be 1..128 characters')
    return v

def sequence(v, high):
    if type(v) is not list or len(v)>high: raise ValueError('invalid or oversized list')
    return v

def pairs(xs):
    d={}
    for k,v in xs:
        if k in d: raise ValueError('duplicate JSON key: '+k)
        d[k]=v
    return d

def read(path, limit):
    with open(path,'rb') as f: b=f.read(limit+1)
    if len(b)>limit: raise ValueError('input too large')
    return b

def load(path):
    return json.loads(read(path,1048576).decode('utf8'), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');a=p.parse_args()
    try: print(json.dumps(analyze(load(a.input)),ensure_ascii=True,indent=2));return 0
    except (ValueError,OSError,UnicodeError,RecursionError) as e:
        print(json.dumps({'error':str(e)}),file=sys.stderr);return 2

if __name__=="__main__": raise SystemExit(main())
