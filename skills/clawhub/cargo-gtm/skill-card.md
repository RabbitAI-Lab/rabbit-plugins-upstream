## Description:

Supports consent-aware B2B go-to-market research, contact enrichment and verification, lead qualification, permission-based outreach drafting, CRM synchronization, and buying-signal monitoring in Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sales and go-to-market teams use Cargo GTM to research target accounts and buying committees, verify B2B records from licensed providers, prioritize leads, draft outreach, and sync approved data with a CRM. Person-related workflows are gated by consent basis, suppression checks, and volume limits; bulk unsolicited messaging and consumer targeting are refused.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The import recipe can change older contact records outside the requested import.

Mitigation: Restrict the query and write-back to the current import's exact record IDs, then review proposed changes before applying them.

Risk: Incorrect contact identity or unapproved data sharing, messaging, or recurring spend could affect people or incur costs.

Mitigation: Independently check contact identity before activation, authorize external data sharing, and explicitly approve messaging actions and recurring budgets.

## Reference(s):

- [Cargo GTM on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Acceptable use](artifact/references/acceptable-use.md)
- [Cost discipline](artifact/references/cost-discipline.md)
- [Output retrieval](artifact/references/output-retrieval.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, JSON, Shell commands]

**Output Format:** [Research and execution guidance, structured account or contact data, outreach drafts, and Cargo CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by requested workflow; may include account and contact lists, research, lead scores, outreach drafts, and run receipts.]

## Skill Version(s):

2.3.2 (source: server-resolved release evidence, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
