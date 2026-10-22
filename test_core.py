import itertools, unittest
from difference_bound_witness import analyze

class Bounds(unittest.TestCase):
    def test_small_graphs_against_independent_floyd_oracle(self):
        for weights in itertools.product(range(-1,2),repeat=3):
            edges=[dict(id=str(i),**{'from':str(i),'to':str((i+1)%3),'max':w}) for i,w in enumerate(weights)]
            d=[[0 if i==j else 100 for j in range(3)]for i in range(3)]
            for i,w in enumerate(weights):d[i][(i+1)%3]=w
            for k in range(3):
                for i in range(3):
                    for j in range(3):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
            r=analyze({'variables':['0','1','2'],'constraints':edges})
            self.assertEqual(r['feasible'],all(d[i][i]>=0 for i in range(3)))
            if r['feasible']:
                for e in edges:self.assertLessEqual(r['assignment'][e['to']]-r['assignment'][e['from']],e['max'])
            else:
                self.assertLess(r['sum_max'],0)
                self.assertEqual(sum(e['max']for e in r['cycle']),r['sum_max'])
                for i,e in enumerate(r['cycle']):self.assertEqual(e['to'],r['cycle'][(i+1)%len(r['cycle'])]['from'])
    def test_disconnected_cycle_is_detected(self):
        r=analyze({'variables':['idle','a','b'],'constraints':[{'id':'ab','from':'a','to':'b','max':-3},{'id':'ba','from':'b','to':'a','max':2}]})
        self.assertFalse(r['feasible']);self.assertEqual(r['sum_max'],-1)
    def test_parallel_edges_and_negative_self_loop(self):
        r=analyze({'variables':['a','b'],'constraints':[{'id':'loose','from':'a','to':'b','max':5},{'id':'tight','from':'a','to':'b','max':-2}]})
        self.assertTrue(r['feasible']);self.assertEqual(r['slacks'][1]['slack'],0)
        r=analyze({'variables':['a'],'constraints':[{'id':'self','from':'a','to':'a','max':-1}]});self.assertEqual([e['id']for e in r['cycle']],['self'])
    def test_empty_constraint_set_and_zero_cycle(self):
        self.assertEqual(analyze({'variables':['x'],'constraints':[]})['assignment'],{'x':0})
        self.assertTrue(analyze({'variables':['x'],'constraints':[{'id':'s','from':'x','to':'x','max':0}]})['feasible'])
    def test_invalid_identifiers_types_and_limits(self):
        for d in [{'variables':['x','x'],'constraints':[]},{'variables':[],'constraints':[]},{'variables':['x'],'constraints':[{'id':'e','from':'x','to':'absent','max':0}]},{'variables':['x'],'constraints':[{'id':'e','from':'x','to':'x','max':True}]},{'variables':['x'],'constraints':[],'extra':1}]:
            with self.assertRaises(ValueError):analyze(d)

if __name__=='__main__':unittest.main()
