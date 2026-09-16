# Argument and Seam Criteria

Focus: does candidate behavior fulfill one need, and is the seam well placed? These groups
synthesize Jackson's material; they are not the author's prescribed sequence.

## Argument Before Seam

Under stated assumptions, trace how actions and state support the OP and why the observable result
fulfills the purpose. Test hidden conditions, skipped steps, and counterexamples from real
scenarios. Keep weak evidence open; a better-written purpose cannot repair missing behavior.

“Delete moves an item to Trash” explains storage change. If the purpose is recovery from accidental
deletion, both OP and contract must include recovery. Implementing the move perfectly still does not
establish the purpose.

## Qualification

| Criterion             | Decision basis                                                                       |
| --------------------- | ------------------------------------------------------------------------------------ |
| User-perceivable      | a user, including an API programmer, experiences value                               |
| Semantic/behavioral   | meaningful dynamic capability rather than a control, category, or property           |
| Purposeful/end-to-end | independently creates an evaluable result that fulfills a need                       |
| Specific              | one indivisible purpose; conflation suggests splitting                               |
| Complete              | enough behavior to fulfill the purpose; fragmentation suggests merging or completing |
| Independent           | definition needs no other concept; shared identity uses field-free type parameters   |
| Familiar              | prefer known concepts and conventions unless a new one provides unavailable value    |

Test reusability after composition. It is often a result of a sound seam, never sufficient evidence
by itself. A concept keeps its name, purpose, and behavioral meaning across applications.

Entities are usually state types; tables, classes, and microservices are implementation
organization; verbs such as register are usually actions; stories and workflows are scenario slices;
cross-concept triggers are synchronizations. Names are clues, not proof.

Use split/merge to adjust control and simplicity, unify/specialize to adjust generality and fit, and
tighten/loosen to adjust automation and user control. Tie the latter to a concrete under- or
over-synchronization scenario.

For every candidate record one outcome with evidence: keep, split, merge, parameterize, demote to
type/action/implementation, move to synchronization, or leave open.
