## Description:

Reconciles company and brand identities across public domains, LinkedIn profiles, SEC registrants, and employer records while preserving ambiguous names and organizational relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to deduplicate supplied company records or a bounded discovery set and build a reviewable mapping of entities, aliases, and relationships. It preserves supporting sources, dates, and unresolved conflicts rather than merging records on name similarity alone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers, queries, and scraped public URLs are sent to Crawlora with an API key.

Mitigation: Avoid submitting confidential customer lists or sensitive business records unless the data-handling requirements permit it; keep the key private.

Risk: Similar names or shared web infrastructure can cause distinct legal entities, brands, and subsidiaries to be incorrectly merged.

Mitigation: Require corroborating evidence, preserve source IDs and dates, and mark uncertain relationships as unresolved.

Risk: Unbounded lookups can consume Crawlora credits and introduce stale or irrelevant evidence.

Mitigation: Limit calls and pages to the requested scope and credit budget, and record observation times separately from source dates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/company-identity-reconciliation)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown tables and evidence ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes canonical records, an alias and ID crosswalk, relationships, source dates, conflicts, and missing lookups.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
