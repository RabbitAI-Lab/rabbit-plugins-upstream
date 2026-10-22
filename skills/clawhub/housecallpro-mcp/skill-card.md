## Description:

Guides users through reading their own Housecall Pro estimates and invoices with curl, summarizing charges, and declining estimate options when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and their assistants use this skill to inspect estimates or invoices sent by their contractor, understand amounts due, and optionally decline a quoted option without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A document link is a bearer credential that can expose customer details and permit declining an estimate.

Mitigation: Use only links you are authorized to access; keep tokens out of shared transcripts, logs, and repositories.

Risk: Declining an option is a real action visible to the contractor.

Mitigation: Review the option and confirm intent before declining; re-read the estimate afterward to check its status.

Risk: The reference material lists unverified account, media, service-agreement, and communications endpoints beyond the reading task.

Mitigation: Avoid those endpoints unless you have clear authorization and a concrete need.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Text guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples retrieve document JSON and summarize amounts; declining an option is an explicit, live action.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
