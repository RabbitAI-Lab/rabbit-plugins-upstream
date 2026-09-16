---
name: concept-design
description:
  Designs Daniel Jackson concepts, purposes, operational principles, state, actions, and
  synchronizations only when the user explicitly invokes $concept-design. Use to turn verified needs
  into an independent concept model and tested application composition.
metadata:
  language: en
  translation_of: concept-design-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-design
---

# Concept Design

Focus: what need must the application satisfy, and which independent concepts and synchronizations
can fulfill it? Run only on explicit `$concept-design` invocation. Deliver the model, then continue
into PRD or implementation only when already authorized.

## Model

A **concept** is a coherent behavioral unit designed for one purpose; pages, entities, and code
modules are only candidate clues.

- A **concept purpose** is an evaluable need explaining why one concept exists.
- The **application purpose** is the outcome a product should create through concept selection and
  composition; it is not the sum of concept purposes.
- An **operational principle (OP)** is a representative, discriminating scenario showing how
  behavior fulfills the concept purpose.
- **State and actions** define allowed behavior through invariants, preconditions, effects, and
  result cases.
- A **synchronization** connects completed concept actions to subsequent calls as an application
  rule.
- A **misfit** is a mismatch between designed behavior and the actual need.

The required argument is: contract supports OP; OP fulfills concept purpose; selected concepts and
synchronizations support application scenarios; scenario outcomes fulfill application purpose.
Composition must preserve each concept's allowed behavior. Facts require sources; label inferences
and unresolved decisions.

## Design Loop

1. **Establish facts** — Identify beneficiaries, application purpose, current state, desired
   outcome, and constraints. In an existing system, trace actual entry points, state ownership,
   failure paths, and tests. Separate current from desired behavior.
2. **Define candidates** — Read `references/spec-format.md`. Clarify terms and write the purpose,
   OP, minimum state, and complete actions. Test meaning with concrete scenarios; represent external
   identity through type parameters.
3. **Review arguments and seams** — Read `references/criteria.md`. Test the contract/OP argument and
   counterexamples, then specificity, completeness, independence, and familiarity. Record a reasoned
   seam decision for every candidate.
4. **Test composition** — Read `references/sync-notation.md`. Starting from application purpose and
   end-to-end scenarios, select and instantiate concepts; define entry, binding, response,
   concurrency, and failure behavior. Check under- and over-synchronization and derive both
   synchronization and product-dependency diagrams.
5. **Revise and deliver** — Correct evidenced misfits using the adjustment moves in the criteria.
   Preserve unresolved assumptions with evidence and impact; block only the dependent portion.

## Output

```markdown
## Application Purpose and Scenarios

<users, purpose, current state, outcome, constraints; sources/inferences/open decisions> <end-to-end
scenarios: condition → actions and syncs → observable result → purpose; misfits>

## Concepts

<purpose, state, actions, OP, optional queries/notes per references/spec-format.md> Argument: <why
contract supports OP and result fulfills purpose; counterexamples/open points> Seam:
<specificity/completeness/independence/familiarity conclusion and reasons>

## Synchronizations

<app/include/sync grouped by entry point or rule responsibility>

## Synchronization Diagram and Product Subsets

<when → rule → then; where reads marked separately> <A → B means including A requires B; MVP>

## Exclusions and Open Decisions

<candidate/action/assumption, conclusion, source, impact>
```

Concept sections remain independent of other concept definitions. Put application context in notes
and coordination in synchronizations. Signatures, result cases, and state relations form the
synchronization interface; an OP is representative rather than exhaustive.

Completion requires evidence for both concept and application purposes, parseable
includes/actions/queries/parameters/outputs/bindings, explicit success and refusal behavior where
responses are required, loop and exclusion policies, faithful multi-source/multi-target/query edges,
and an MVP closed over entry points, remaining rules, dependencies, and resources. For a first full
example read `references/example-reserving.md`; for source definitions read `references/sources.md`.
