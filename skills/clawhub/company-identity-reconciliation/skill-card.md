## Description:

Reconciles company and brand identities across public domains, LinkedIn company profiles, SEC registrants, and employer records while preserving evidence and entity distinctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to deduplicate company lists and create reviewable identity crosswalks, retaining source evidence and distinctions between legal entities, brands, parents, and subsidiaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, domains, public URLs, IDs, and lookup parameters are sent to Crawlora under the user's API key.

Mitigation: Use only with authorization to share lookup inputs with Crawlora and safeguard the API key.

Risk: Unbounded lookups can consume API credits, and mistaken identity matches can affect business records.

Mitigation: Bound discovery scope and credit budget; review the evidence-backed mapping before updating any business system.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/company-identity-reconciliation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Reviewable tables and evidence ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canonical records, alias and ID crosswalk, relationships, conflicts, and missing lookups; does not authorize changes to business systems.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
