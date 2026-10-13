# Nanobody design

## Purpose and scope

Design VHH candidates from an antigen structure with BoltzGen, mBER, and RFantibody, evaluate a selected candidate set with common methods, and deliver Pareto-ranked candidates and corresponding structures.

This Guide specifies the intended business workflow. Verify that available capabilities support its methods and input/output requirements; method names here do not establish current platform availability. Use the main skill for discovery, submission, observation, and result retrieval. Preserve the three design branches and evaluation methods when carrying out this workflow; a reduced or substituted workflow requires an explicit change of scope.

For explanation or planning requests, describe the relevant choices without preparing computation. For an execution request, resolve only missing inputs or decisions that affect the work; reuse the user's established choices.

## Inputs and decisions

- Antigen structure and the actual antigen chains to include. Inspect the structure; resolve “all chains” to the observed chain set.
- Binding hotspot, or an explicit choice to leave it unspecified. Record the structure, chain, and residue numbering to which any hotspot refers.
- Design count. Distinguish generation samples, template runs, and retained outputs when estimating the number of candidates and the workload; verify whether each count applies per template or across the job.
- TopN candidates per design source for evaluation; proposed default: 100, taking all candidates when fewer are available. Use an applicable default when consistent with the user's scope and budget.
- For a multichain antigen, the single antigen chain used by RFantibody. This choice changes the modeled system and must follow the user's objective and evidence.

Keep documented method defaults for other settings where compatible with this workflow. Retain the effective method settings with the results so that comparisons can be interpreted.

The ordinary BoltzGen branch uses about 1,000 generation samples regardless of a smaller final output count; a small requested output is not a promise of a short run. TopN controls subsequent evaluation coverage, not the upstream design sampling. Assess design and evaluation workloads separately against the user's budget and time constraints, and preserve uncertainty about queueing and runtime. Report actual delivered candidate counts rather than treating configured per-template limits as completed output.

## 1. Prepare the antigen

Renumber the selected antigen structure for downstream design. Retain the relationship between original and prepared chain/residue identifiers. Map hotspots through this relationship; do not reuse residue numbers merely because they look unchanged.

BoltzGen and mBER use the prepared antigen with the selected chains. Prepare a single-chain antigen for RFantibody when necessary. Verify that the resulting structure contains the intended chains and residues before using it.

## 2. Generate candidates

The three design branches are independent once their inputs are ready.

| Method     | Intended configuration and constraints                                                                                                                                                                                                        |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BoltzGen   | De novo nanobody design using the prepared antigen, selected antigen chains, design count, and hotspot if specified. This workflow uses 1,000 samples.                                                                                        |
| mBER       | Nanobody design using the prepared antigen, resolved chain selection, design count, and hotspot if specified. The method may default to all chains; record the actual selected chain set for reproducibility.                                 |
| RFantibody | De novo nanobody design with a single-chain antigen. This workflow uses sequential antigen residue numbering from 1 for hotspots and a design count per template. Verify this convention and the effective template set before applying them. |

The current mBER contract permits an unspecified hotspot; this neither proves nor disproves runtime compatibility for every multichain input. If a specific incompatibility is established, identify it. An explicit hotspot or a single-chain input may define an alternative, but selecting either changes a scientific input and requires a resolved user choice. Do not reject all such inputs based only on a historical failure or silently drop antigen chains to make a branch run.

Obtain each branch's candidate structures, complex sequences, and selection metrics. Preserve candidate identity and source across these outputs. A failed branch is incomplete coverage, not an empty successful result.

## 3. Select candidates and prepare common evaluation

Select up to TopN candidates independently from each source:

| Source     | Selection rule                            |
| ---------- | ----------------------------------------- |
| BoltzGen   | Published final design rank, lower first. |
| mBER       | ipTM, higher first.                       |
| RFantibody | ipAE, lower first.                        |

Do not substitute file order when selection metrics or candidate mappings are missing. Resolve any tie at the selection boundary consistently and retain the rule used.

Build one selected candidate set with corresponding structures and complex sequences. Both representations must refer to the same candidates; taking the first TopN sequence records independently is insufficient. Retain source identity and distinguish antigen chains from VHH chains for every candidate.

Convert structure formats and normalize chain identifiers only as required by the evaluation methods, preserving molecular identity and an explicit mapping. If complex sequences must be derived from structures, account for unresolved residues and chain order rather than assuming that observed coordinates represent the complete intended sequence.

Use these evaluations:

| Evaluation                                   | Input and intended settings                                                                                                                        |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Binding Free Energy (dG)                     | Selected complex structures, with VHH chain(s) identified as the ligand. Normalize ligand chain identifiers if a shared batch setting requires it. |
| OpenDDE                                      | Selected complex sequences in batch mode; seed 39 and the antibody-antigen checkpoint `abag`.                                                      |
| Protenix v2.0                                | The same selected complex sequences in batch mode; seed 39.                                                                                        |
| DeepRank-Ab antibody-antigen complex scoring | Two-chain scoring structures: antigen A and VHH B. For a multichain antigen, select the antigen chain with the most CA contacts to the VHH.        |

For a multichain antigen requiring DeepRank-Ab projection, resolve the contact criterion and tie handling from the applicable method contract or a user decision before selecting an antigen chain; this Guide does not prescribe them. A complex with one identified antigen chain and one VHH needs no additional antigen-chain selection decision. Preserve the original complex and chain mapping, and disclose any reduction of the antigen system. An empty interface or unavailable valid projection is an evaluation gap, not a reason to choose an arbitrary chain.

Verify the effective batch limits and that every selected candidate is covered. Retrieve the resulting metrics with their candidate correspondence; a completed job alone does not prove complete candidate coverage.

## 4. Merge metrics and rank

Match evaluation records to the selected candidate identities. Exclude aggregate summary rows. When Protenix produces multiple ranked predictions per candidate, retain the one with the highest Ranking Score, keeping its associated metrics together. Do not merge unrelated records merely because normalized names collide.

Use these six objectives for Pareto ranking:

| Metric                          | Preferred direction |
| ------------------------------- | ------------------- |
| dG binding energy (`WT_G_bind`) | Lower               |
| OpenDDE Confidence Score        | Higher              |
| OpenDDE ipTM                    | Higher              |
| Protenix Ranking Score          | Higher              |
| Protenix ipTM                   | Higher              |
| DeepRank-Ab Predicted DockQ     | Higher              |

Use the Pareto method's `equal` missing-value policy: when a compared objective is missing, that dimension is treated as equal and does not decide the comparison. Confirm that the selected method retains this meaning and report missing evaluation coverage separately; this does not impute a score or establish complete evaluation. The policy governs Pareto comparisons, not the secondary mean-rank ordering below.

For complete metric records, compute a rank for each objective using the directions above, assigning average ranks to ties. Compute the mean of the six ranks. Order candidates first by ascending Pareto rank, then by ascending mean rank. Retain unresolved ties as ties.

If any objective is missing, resolve how that affects the secondary mean-rank ordering before producing a final ordered result. Do not silently average fewer objectives or assign different penalties to missing values based on row order.

## Deliverables and interpretation

- Final candidate score table containing source identity, the six metrics, missing coverage, Pareto rank, per-metric ranks, and mean rank where defined.
- Structures corresponding to all ranked candidates, with an explicit correspondence to the table.
- Structures for the first Pareto front.
- Effective inputs and method settings, candidate counts by source, chain/residue mappings, and any incomplete branches or evaluations needed to interpret the results.

Report the first-front count and leading candidates from the delivered evidence. Keep design-model selection scores distinct from common evaluation scores. Describe the ranking as a computational prioritization under these methods and objectives; it does not establish experimental binding, affinity, or developability.
