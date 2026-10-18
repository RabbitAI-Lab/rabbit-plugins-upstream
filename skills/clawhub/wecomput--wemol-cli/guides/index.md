# Task Guides

Choose a Guide by the user's objective and available inputs. Read only the matching Guide; if none applies, continue using the main skill. Routine job queries and artifact retrieval do not require a task Guide.

| Guide | Use when |
| --- | --- |
| [Structure prediction](structure-prediction.md) | Predicting structures from sequences, including chain organization and comparison within a maintained multi-model workflow. |
| [Antibody humanization](antibody-humanization.md) | Humanizing an existing conventional antibody or VHH and interpreting proposed substitutions. |
| [Affinity maturation](affinity-maturation.md) | Optimizing an existing antibody against a target while preserving specified mutation constraints. |
| [Antibody developability QC](antibody-developability-qc.md) | Screening existing antibody or VHH candidates for documented developability risks. |
| [Immunogenicity prediction](immunogenicity-prediction.md) | Assessing supplied sequences with an immunogenicity prediction method or interpreting its results. |
| [De novo antibody design](de-novo-antibody-design.md) | Generating antibody candidates with BoltzGen, including choosing ordinary or high-throughput design. |
| [Nanobody design](nanobody-design.md) | Planning or carrying out de novo VHH design from an antigen structure using three design methods, common evaluation, and Pareto ranking. |
| [Peptide design](peptide-design.md) | Generating peptide candidates for a target; distinguish peptide products from protein binders. |
| [Molecular dynamics](molecular-dynamics.md) | Simulating a protein or protein–ligand system, or analyzing an existing trajectory for a stated question. |
| [Small-molecule docking](molecular-docking.md) | Exploring receptor–small-molecule binding poses with a defined binding-site strategy. |

Match the requested scope as well as the molecule type. A VHH request naming BoltzGen belongs to the BoltzGen Guide; use the three-method nanobody Guide for that broader design-and-evaluation workflow. Do not expand a single-method request into the three-method pipeline. Existing-candidate humanization, QC, or affinity optimization is not de novo design. For a task spanning several stages, read additional Guides only when those stages serve the user's goal; do not load the whole catalog.

Guides define business workflows, not command syntax or execution mechanics. Preserve the user's scope: explaining a workflow does not authorize running it. For an applicable workflow, preserve its specified methods, dependencies, and evaluation rules while planning concrete operations through the main skill and current capability contracts. If a required method or transformation is unavailable or incompatible, report the gap; do not silently substitute a different scientific workflow.
