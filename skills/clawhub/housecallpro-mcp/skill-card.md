## Description:

Guides customers in reading Housecall Pro estimates and invoices with shell commands, checking what is owed, and declining estimate options without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to inspect contractor-sent estimates and invoices, summarize charges and amounts due, and optionally decline an estimate option from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links function as bearer credentials and can expose customer documents or allow an option to be declined.

Mitigation: Keep links and tokens out of shared transcripts, logs, and repositories; use only links you are authorized to access.

Risk: The reference material lists unsupported account, media, service-agreement, and communications endpoints beyond the customer-document task.

Mitigation: Avoid those unsupported endpoints unless you have a clear authorized reason to use them.

Risk: Declining an estimate option notifies the contractor and cannot be reversed through this skill.

Mitigation: Review the estimate and selected option before declining, then re-read the document to confirm its status.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/housecallpro-mcp)
- [Housecall Pro consumer API recipes](artifact/references/recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides document summaries and instructions for verifying a declined option; approval must be completed in a browser.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
