---
name: entity-resolution
description: Match provider, facility, organization or device entities across sources and resolve field conflicts using identifiers, provenance and time. Use for identity and relationship questions, including uncertain matches; a source name alone is not a matching key.
license: MIT-0
---

# Entity matching and source conflicts

Determine whether records describe the same entity, related entities, different entities or an unresolved case. Preserve evidence and the cost of false merges.

## Establish the matching contract

Identify the required entity grain, geographic/time scope and identifier namespace. A clinician, corporation, billing group, campus and health system can have similar names and different identities. Relationships do not collapse those entities.

Inspect actual fields and known source semantics. Retain originals separately from normalized names, addresses, dates and identifiers. IDs are strings; check their issuer and entity type. An identifier is strong evidence only when its namespace, integrity and scope fit the task. Conflicting authoritative identifiers or types require investigation, not an automatic override.

## Generate and assess candidates

Use complementary available signals: supported identifiers, aliases, location, specialty, organization relationships and dates. Names-only blocking can omit renamed or transliterated entities. Keep candidate-generation misses distinct from wrong pairwise decisions.

Compare evidence for and against each plausible match. A shared practice address is weak identity evidence for individual clinicians. A moved address may reflect time rather than a different person. Translate/transliterate names when relevant, retaining the original and corroborating identity.

Return one of:
- Same entity, with supporting identifier or sufficient corroborating evidence.
- Related entities, with the relationship and distinct IDs.
- Different entities, with decisive contradictory evidence.
- Unresolved, with the smallest additional evidence that could distinguish the alternatives.

A similarity score is not a calibrated probability. Do not invent confidence percentages or identifiers. An empty candidate list proves only that the current candidate generator found none.

## Resolve fields by their meaning

Choose authority for each field and relevant time, not a single winner for the entire record. A registration source may establish identifier/type; a dated facility roster may support current affiliation; a licensing authority supports licensure. An NPI alone does not establish a current license or credentials.

Keep source value, normalized value, publisher, location and observation/effective date. Retrieval date is not the fact's effective date. Preserve historical values and contradictions. A newer page is not necessarily more authoritative for every field.

If a plausible match remains ambiguous, retain both records or an unresolved match result as the output requires. Do not silently assign it to a convenient existing entity. Trace whether a failure began in source parsing, normalization, candidate generation, pairwise scoring or clustering before changing the rules.

## Verify and deliver

Measure supported match errors and candidate misses using appropriately labeled examples. Pairwise precision alone does not establish full-pipeline recall. Clusters need consistency checks: accepting A=B and B=C can incorrectly imply A=C.

Deliver the crosswalk, relevant relationship/field decisions and unresolved cases, with a concise explanation of downstream impact. A review queue is optional and must serve the requested workflow, not replace the matching output.

See [worked example](references/example.md) or [practice](references/practice.md) when useful. During coaching, ask for a decision and evidence, then explain the consequence of the missed distinction.

