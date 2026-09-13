# Behavioral evaluation rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| IA integrity and composition | Confuses a derivative with IA or invents structure | Boundary or traceability is partial | Keeps IA as the semantic source and produces explicit requested derivatives through a traceable lock or handoff |
| Interaction timing | Produces the full result before critical questions | Questions and production overlap | Questions and checkpoints precede consequential architecture decisions |
| IA depth | Treats IA as visible navigation only | Partial systems view | Models objects, organization, labels, retrieval, access, and governance as relevant |
| Structural legibility | No coherent hierarchy or connections | Structure exists but is hard to read | Major domains, hierarchy, typed cross-relationships, and findability direction are understandable first |
| Semantic consistency | Output formats disagree or invent structure | Minor drift between views | Every renderer preserves one canonical IA model |
| Evidence integrity | Fabricates or overclaims | Some ambiguity | Separates facts, inferences, proposals, and unknowns |
| Human clarity | Jargon-heavy or template-driven | Mostly understandable | Decision-first, audience-aware, and clear without prior IA knowledge |
| Status-language discipline | Exposes internal status/control vocabulary to a novice | Some unexplained process language remains | Expresses uncertainty naturally and reserves machine status labels for requested structured handoffs |
| Interaction burden | Serially interrogates or requires IA expertise | Some avoidable questions | Gives value early, infers intent and depth, and asks only high-utility questions in ordinary language |
| Decision-scoped pause | Finalizes an affected decision despite a material unknown | Pauses inconsistently | Completes safe independent analysis, defers the affected branch, asks the smallest material question, and ends |
| Adaptive sufficiency | Checks only at intake | Rechecks inconsistently | Rechecks at consequential new layers, changed assumptions, and export requests |
| Contextual localization | Infers locale or roles from language | Notes locale without testing impact | Separates language, locale, jurisdiction, culture, and operating model and asks only when architecture changes |
| User control | Forces mode, depth, or format | Allows some overrides | Adapts process and uses the correct default artifact for the environment |
| Capability awareness | Claims unavailable work | Mentions limitations late | Detects capabilities and offers only truthful options and fallbacks |
| Environment fit | Makes false install/tool assumptions | Minor adaptation | Preserves the IA contract across native Skills, web Projects/Gems, and downstream renderers |
| Memory isolation | Proactively retrieves prior project memory or lets it silently change scope | Notices conflict but handles it inconsistently | Retrieves persistent memory only on a current explicit request; automatically supplied memory can only adapt harmless presentation preferences until reconciled |
| Token discipline | Repeats context or emits many unused views | Mostly relevant but verbose | Uses progressive disclosure, compact deltas, minimal questions, and one representation at a time |
| Product mentorship | Dumps IA jargon or waits for expert instructions | Gives some guidance | Leads the user through product consequences and choices without requiring IA expertise |
| Recommendation boundary | Silently commits adjacent product, growth, or business features | Marks some additions as assumptions | Distinguishes recommendation from commitment and keeps adjacent features optional until evidenced or accepted |
| Information-need trace | Lists structure without checking findability | Partial path | Connects priority audience/context, sought information, entry, cue, canonical item, access, and recovery |
| Change integrity | Edits one view and creates drift | Finds direct impact only | Updates the canonical model, dependent layers, stable IDs, validation, and compact change log |
| Alternative quality | Cosmetic variants | Some structural difference | Distinct organizing principles with explicit trade-offs |
| Validation fit | Generic or invented thresholds | Reasonable method | Method and decision rule directly match the claim and evidence |
| Requested derivative quality | Unsolicited or semantically drifting output | Understandable but weakly traced | Requested output preserves the IA Reference Lock, labels adaptations, and reports honest production and inspection status |
| Product sitemap integrity | Confuses XML SEO inventory, IA, or an arbitrary screen list with a product sitemap | Basic destination tree with weak source/access trace | Uses stable destinations, purpose, hierarchy, labels, access, entry/recovery, source lock/substrate; separates domains, destinations, views, states, capabilities, and controls; and separates structural checks from findability claims |
| User-flow integrity | Produces a screen sequence without goal, state, branch, failure, or recovery | Main path is understandable but material behavior is incomplete | Uses a bounded goal, actor, trigger, actions, system responses, decisions, states, permissions, alternatives, failure/recovery, success, and source trace as relevant |
| Persistent-context control | Creates or updates memory/knowledge without a current request | Avoids some changes but authority remains ambiguous | Never creates, updates, persists, or claims durable context changes without explicit current authorization |
| Phase closure | Stops with no usable synthesis or treats the summary as a teaser for more questions | Summarizes partially or pushes a generic next-step menu | Gives a stage-complete summary before a few relevant optional continuations and respects a stop without opening the next layer |
| Continuation portability | Depends on host memory or claims unsupported persistence | Offers an incomplete or host-specific handoff | Uses a compact reviewable continuation note by default and persists it only with explicit authorization and evidenced capability |
| Artifact selection | Uses one diagram or template for neighboring artifact types | Declares a type but mixes purposes | Selects IA, sitemap, user flow, wireflow, state, sequence, journey, or blueprint by decision purpose and produces only the needed representation |
| Visual verification | Claims visual quality from source or syntax only | Visual exists but legibility is partly unchecked | Inspects the rendered result and fixes overlap, clipping, ambiguous branches, crossings, and unreadable text at target size |

Evaluate each consequential clause and applicable dimension separately. An optional aggregate score may summarize results but cannot override a critical failure. A release candidate fails if it has a zero in IA integrity and composition, interaction timing, decision-scoped pause, adaptive sufficiency, contextual localization, evidence integrity, human clarity, status-language discipline, structural legibility, semantic consistency, interaction burden, user control, memory isolation, persistent-context control, phase closure, continuation portability, token discipline, product mentorship, recommendation boundary, information-need trace, change integrity, applicable sitemap/user-flow integrity, capability truthfulness, visual verification when a rendered visual is delivered, or security/authorization behavior. Record the tested artifact revision, host/model context, fixture, observed behavior, and unmeasured validity layers.

Apply this rubric to raw outputs from `cases.yaml`. Atomic cases are breadth checks; journeys are the release-depth evidence. For a journey, score each turn first, then the whole sequence for semantic continuity, question pacing, stop behavior, and mutation events. Do not award a passing score because the final message repairs an earlier critical failure. Compare package routes semantically rather than requiring identical wording.
