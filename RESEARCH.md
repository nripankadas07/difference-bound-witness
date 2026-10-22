# Research — 22 October 2026

Demand is **inferred** from this workflow: A set of individually plausible timing rules can be mutually impossible, without showing the exact contradictory bounds.

[Exact stars-desc GitHub query](https://github.com/search?q=difference%20constraints%20sort%3Astars-desc&type=repositories), observed 2026-10-22T06:18:36.315Z. Highest-star relevant comparable found in the inspected pool: `networkx/networkx`. Keywords are narrow; established comparables were supplemented directly. The difference-constraints keyword results were mostly unrelated and do not establish market coverage.

| Comparable | Stars | Last push | GitHub license metadata | Workflow and setup |
| --- | ---: | --- | --- | --- |
| [networkx/networkx](https://github.com/networkx/networkx) | 17347 | 2026-10-22T00:46:41Z | NOASSERTION | Python graph algorithms including a negative-cycle witness; pip installation and documented examples. |
| [google/or-tools](https://github.com/google/or-tools) | 14244 | 2026-10-21T10:10:54Z | Apache-2.0 | C++ optimization suite with Python/.NET/Java APIs and solver-specific installation and examples. |
| [Z3Prover/z3](https://github.com/Z3Prover/z3) | 12807 | 2026-10-22T05:39:30Z | NOASSERTION | SMT theorem prover with binaries, bindings and richer theories; README states MIT while GitHub metadata is inconclusive. |

## Choice and tradeoffs

Produce a feasible integer assignment or an edge-ID negative-cycle contradiction for difference constraints. activity-slack-report computes critical paths on a precedence DAG with durations. This is an independent numeric constraint satisfiability tool with two-sided relative bounds encoded as edges and contradictory-cycle proofs, including cyclic feasible systems. No task durations, CPM or slack scheduling UI is reproduced.

The established alternatives are broader and may be the right choice for their supported ecosystem. Our small CLI offers one dependency-free runtime and an inspectable JSON report for the stated subset. It sacrifices generality and may reject valid real-world input outside that subset. READMEs/current docs/source and sampled issues were inspected for workflow context; this does not prove competitor feature absence. ATL explicitly supports WAV CUE/LIST, NetworkX explicitly returns negative cycles, and RLEMaskLib performs mask operations without full raster expansion. Our example proves only our behavior.

Installability and first-result instructions are documented above and in upstream READMEs. Competitor clean installs, time to first useful result, reliability, support response and performance were **not measured**. No superiority, adoption or global ranking claim. Stars are research context only. [Exact provenance and sampled issues/PRs](RESEARCH_PROVENANCE.json). Inconclusive GitHub license metadata is not a legal conclusion; NetworkX README states BSD3, Z3 README MIT, and Knossos README EPL. No implementation is reused.

Primary references:
- https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.find_negative_cycle.html
