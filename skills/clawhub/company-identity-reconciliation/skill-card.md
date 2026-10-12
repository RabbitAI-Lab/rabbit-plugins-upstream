## Description:

Reconciles company and brand identities across public domains, LinkedIn profiles, SEC registrants, and employer records using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business-data teams use this skill to deduplicate supplied company and brand records into a reviewable identity crosswalk, preserving source IDs, relationships, conflicting evidence, and observation dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, domains, IDs, URLs, and lookup targets supplied to the skill are sent to Crawlora's external API using the user's API key.

Mitigation: Use only public or approved business identity data and limit queries to the authorized scope.

Risk: Ambiguous names or shared branding can produce incorrect entity matches if a crosswalk is applied without review.

Mitigation: Keep source evidence and relationship distinctions, and review mappings before updating operational systems.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/company-identity-reconciliation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and an evidence ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped canonical records, alias and ID crosswalk, relationship decisions, conflicts, missing lookups, and source dates for review.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
