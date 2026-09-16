# Synchronization Semantics and Composition Checks

Application purpose states the overall need. Concept selection and synchronizations jointly
determine application behavior. Define end-to-end scenarios first, connect completed actions to
later calls, and explain each rule's contribution while preserving every concept contract. The
notation follows WYSIWID record patterns plus documented local extensions; it is not executable
engine syntax.

## Compose

1. Check participating concepts, entry signatures, result cases, and instantiation against
   `spec-format.md`; use `example-reserving.md` to split rules by data dependency.
2. Give each rule one explainable decision. Match only required fields and distinguish success from
   error. Preserve flow and object correlation for multiple `when` records.
3. Check zero/many `where` bindings, all required `then` inputs, and dependencies on future outputs.
   Cover response, refusal, and partial-completion failure for each entry.
4. Simulate concurrency, replay, and loops. Authorization and validation precede writes; state
   queries never replace atomic action invariants.

## Flow and Coverage

A runtime flow is one causal instance rooted in an external event. Requesting expresses requests;
timers and messages declare their own roots. `// flow:` groups rules by responsibility and rule
identities remain unique.

A synchronization diagram gives every sync a rule node, multiple `when` edges in, multiple `then`
edges out, and separately marked `where` queries. A simplified A→B diagram retains the rule name and
conjunction note and never represents product dependency. Loops need a termination or
controlled-continuation argument; engineering caps must be observable.

Under-synchronization omits required coordination and suggests tightening. Over-synchronization
removes user control and suggests loosening or configuration. Decide from application purpose and a
concrete scenario. Placeholder actions still require contracts. Synergy is additional composition
value; if it distorts a concept's purpose, revisit the seam.

## Product Dependencies

An intrinsic dependency appears inside a concept definition and should be removed by
parameterization or composition. An extrinsic dependency is an application choice: including A is
meaningful only with B; record `A → B` in the overall PRD.

Implementation should support meaningful subsets. Beyond dependency closure, check purpose, entry
points, remaining synchronizations, and external resources. Grouping alone does not make a subset
deliverable; treat cycles as dependency groups.
