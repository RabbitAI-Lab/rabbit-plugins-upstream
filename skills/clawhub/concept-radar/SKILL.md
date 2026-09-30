---
name: concept-radar
version: 0.1.1
description: Discovers, deduplicates, and evaluates evidence-backed concepts. Invoke only when the user explicitly requests this workflow for specified URLs or an author pool.
allowed-tools:
  - WebSearch
  - WebFetch
---

# Concept Radar

## Purpose

Discover concepts from user-specified public URLs or a user-specified author pool, merge duplicates, and evaluate the resulting concepts against public evidence.

## Activation Contract

Invoke only when all of the following are true:

1. The user explicitly asks to discover or identify concepts.
2. The user explicitly asks to deduplicate or consolidate overlapping concepts.
3. The user explicitly asks to evaluate, assess, rank, or qualify the concepts.
4. The user supplies at least one source URL or identifies an author pool to research.

Do not infer this workflow from a general request to browse, summarize, brainstorm, monitor, or research.

### Positive Trigger Examples

- “From these three URLs, discover the main concepts, deduplicate overlaps, and evaluate their maturity and usefulness.”
- “Use this list of authors as the source pool; identify, merge, and assess the concepts they have published.”
- “Scan the specified newsletter URLs for emerging concepts, consolidate synonyms, and evaluate each concept with evidence.”
- “Find concepts discussed by these named researchers, remove duplicates, and rank them by maturity and confidence.”

### Non-Trigger Examples

- “Summarize this article.”
- “Explain this concept to me.”
- “Brainstorm ten product ideas.”
- “Research current AI trends.”
- “Compare these authors’ writing styles.”
- “Extract all links from this page.”
- “Monitor these authors every week.”
- “Save the findings to a file.”
- “Post the results to my team channel.”
- “Evaluate this list of concepts,” when no discovery source URL or author pool is specified.

## Operating Boundary

- Use only `WebSearch` and `WebFetch`.
- Inspect publicly reachable pages within the source boundary and return the result directly in the conversation.
- Keep the workflow read-only and limited to concept discovery, deduplication, and evaluation.

## Source Discipline

1. Keep discovery within the specified URLs or author pool.
2. For an author pool, use `WebSearch` only to locate relevant public works attributable to those authors, then use `WebFetch` to inspect useful sources.
3. Prefer primary sources by the named author or publisher. Use independent sources only to corroborate maturity or adoption.
4. Record the direct URL supporting each material claim.
5. Distinguish author language, paraphrase, inference, and uncertainty.
6. Never invent inaccessible content, publication dates, authorship, adoption, or evidence.
7. If the supplied sources are inaccessible or insufficient, report the limitation and evaluate conservatively.

## Method

1. Restate the source boundary and any evaluation criteria supplied by the user.
2. Inspect the specified URLs or locate relevant public works from the named author pool.
3. Extract candidate concepts only when a source provides enough context for a defensible definition.
4. Normalize candidate names while preserving the source terminology.
5. Deduplicate by comparing meaning, mechanism, intended outcome, and scope—not wording alone.
6. Merge true synonyms and near-duplicates; list aliases and retain all supporting links.
7. Keep related but materially distinct concepts separate. Explain ambiguous merge decisions.
8. Evaluate every retained concept using the rubrics below.
9. Present unsupported dimensions as `Unknown`; do not fill gaps with assumptions.

## Evaluation Rubrics

### Maturity

- **Nascent:** mainly a proposal, isolated observation, or newly coined frame.
- **Emerging:** repeated discussion or early examples exist, but practice and terminology remain unstable.
- **Developing:** multiple implementations, communities, or documented practices exist, with unresolved limitations.
- **Established:** sustained adoption, stable terminology, and substantial independent evidence exist.
- **Unknown:** available evidence cannot support a level.

### Confidence

- **High:** clear primary evidence plus meaningful corroboration; attribution and interpretation are stable.
- **Medium:** credible evidence exists, but coverage, independence, or interpretation is limited.
- **Low:** evidence is sparse, indirect, ambiguous, or primarily self-asserted.

Confidence measures confidence in the assessment, not the concept’s quality or maturity.

## Required Output

Begin with a brief scope note listing the URLs or author pool examined, meaningful access gaps, and the deduplication approach.

For each retained concept, provide:

1. **Concept name**
2. **Definition** — a concise, evidence-grounded explanation.
3. **Aliases and deduplication note** — merged labels, overlaps, and why they were merged or kept separate.
4. **Evidence links** — direct source URLs with a short statement of what each supports.
5. **Maturity** — one rubric level with rationale.
6. **Confidence** — High, Medium, or Low with rationale.
7. **Applicable scenarios** — situations where the concept is plausibly useful.
8. **Boundaries** — non-applicable cases, limitations, assumptions, risks, or unresolved questions.

End with a concise comparison or ranking only when the user requests one or when it materially clarifies the evaluation. Clearly label evidence gaps and contested interpretations.
