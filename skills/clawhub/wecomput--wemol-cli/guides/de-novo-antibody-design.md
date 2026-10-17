# De novo antibody design with BoltzGen

## Goal and scope

Generate antibody candidates from a target and design constraints using the BoltzGen method family. Choose between ordinary design and high-throughput design according to the requested scale, supported molecular product, and target evidence.

This Guide covers that method-specific route. For a VHH project explicitly requiring three design methods, common evaluation, and Pareto ranking, use the [nanobody design Guide](nanobody-design.md). Do not expand an ordinary BoltzGen request into that larger workflow.

## Inputs and choices

- Target sequence or structure accepted by the selected method, with relevant chains and any evidenced interface or hotspot constraints.
- Intended antibody product, design constraints, requested scale, and applicable candidate limits.
- Ordinary versus high-throughput design. Availability of an HTS capability is not itself a reason to choose it.

`Binder Design (BoltzGen)` and `Binder Design (BoltzGen) HTS` identify the intended method family and scale variants. Verify the supported product class, batch semantics, and effective defaults; a generic binder label does not establish antibody suitability.

Distinguish generation samples, template runs, and retained output candidates. The ordinary route documents a fixed generation sample count of about 1,000; reducing the final output count does not reduce that sampling workload proportionally. HTS exposes a separate sampling scale. Verify whether output limits apply per template or across the job before estimating candidate counts. Relate the effective workload to the user's budget and time constraints; do not promise a quick pilot from a small output count or treat one observed queue delay as a fixed runtime. Changing templates or methods to reduce work changes the design scope and must preserve the user's intent.

## Business workflow

1. Establish the target, desired product, and scale from user intent and inspected evidence.
2. Select the compatible ordinary or high-throughput route. Resolve missing target/interface or preservation constraints only where required.
3. Generate candidates with the selected method and obtain sequences, structures, and reported confidence or ranking outputs.
4. Keep candidate-to-target correspondence, particularly across high-throughput batches. Report requested versus returned candidate coverage and incomplete branches.

## Results

Deliver candidate identities and available sequence/structure pairs with documented scores and design settings. Use the method's supported selection criteria or the user's specified criteria; do not add unrelated evaluations solely because they are available.

Generated candidates and their rankings do not establish binding, specificity, or developability. Conceptual comparisons of ordinary and high-throughput design do not require an execution setup.
