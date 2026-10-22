# difference-bound-witness

Produce a feasible integer assignment or an edge-ID negative-cycle contradiction for difference constraints.

For release planners debugging relative minimum/maximum timing rules.

## Quickstart

Python3.10+; no runtime dependencies or external service. The wheel build needs setuptools and wheel from the normal Python registry. Linux shell:

```sh
git clone https://github.com/nripankadas07/difference-bound-witness.git
cd difference-bound-witness
python -m venv .venv
. .venv/bin/activate
python -m pip install .
difference-bound-witness example.json
```

The invented three-bound example proves 0<=-1, and lists the responsible edge IDs. [Expected report](example-output.json).

## Input and interpretation

Start from [example.json](example.json). Inputs are read only. JSON files are UTF8,<=1MiB; duplicate/unknown keys, booleans in integer fields and nonfinite constants reject.

100 variables,1000 constraints, input integers within +/-10^12. Each edge means x[to]-x[from]<=max. Encode a minimum L by reversing an edge with max=-L. Variables are free up to translation; assignments are normalized so their minimum is0, not anchored absolute dates. No calendars, optimal makespan, resources, mixed nonlinear constraints or minimal unsatisfiable core. The returned negative cycle is sufficient but need not be smallest.

Exit0 means analysis completed, including any infeasibility, NOT_LINEARIZABLE, UNKNOWN or reference finding. Inspect the report fields; exit0 is not a health assertion. Exit2 means malformed/unsupported input or I/O failure, with JSON error on stderr and no partial report. No live-system operations, network requests or credential reads occur. Reports may expose supplied identifiers and bytes; review before sharing.

## Verification

```sh
python -m unittest -v
python -m compileall -q difference_bound_witness.py
python -m pip wheel --no-deps . -w dist
```

27 weighted cycles against independent Floyd-Warshall, disconnected/parallel/self-loop bounds, assignment/slack checks and invalid schemas. [Validation record](VALIDATION.md). CI runs Python3.10/3.12/3.14 on Linux and the installed console outside checkout. Windows/macOS, production workloads and competitor performance remain untested.

## Scope and provenance

Alpha utility. Original AI-assisted code and invented fixtures; standard algorithms independently reimplemented. No third-party implementation/prose copied. MIT. [Candidate brief](BRIEF.json), [research](RESEARCH.md), [support](SUPPORT.md), [contributing](CONTRIBUTING.md), [security](SECURITY.md).

activity-slack-report computes critical paths on a precedence DAG with durations. This is an independent numeric constraint satisfiability tool with two-sided relative bounds encoded as edges and contradictory-cycle proofs, including cyclic feasible systems. No task durations, CPM or slack scheduling UI is reproduced.
