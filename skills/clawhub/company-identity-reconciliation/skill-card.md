## Description:

Reconciles company and brand identities across public domains, LinkedIn company profiles, SEC registrants, and employer records while preserving source evidence and ambiguous relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use the skill to deduplicate scoped company lists and build reviewable crosswalks of legal entities, brands, employers, aliases, and related organizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, domains, public URLs, lookup parameters, and an API key are sent to Crawlora.

Mitigation: Use only data you are comfortable sharing with Crawlora and keep the API key private.

Risk: Ambiguous names or shared brand, employer, and parent identifiers can lead to incorrect merges.

Mitigation: Review the evidence ledger and preserve unresolved or related-but-distinct records instead of forcing a match.

Risk: An incorrect mapping could propagate to business systems or public claims.

Mitigation: Bound lookups to the intended records and require separate review before updating systems or publishing claims.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/company-identity-reconciliation)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown tables and evidence ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes canonical records, alias and ID crosswalks, relationship decisions, source dates, conflicts, and missing lookups.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
