## Description:

Guides customers through reading Housecall Pro estimates and invoices with shell commands, including checking amounts owed and declining estimate options without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to inspect contractor-sent Housecall Pro estimates and invoices, summarize pricing and balances, and optionally decline an estimate option from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document links grant access to customer estimates or invoices and can be used to decline estimate options.

Mitigation: Keep links private and out of shared transcripts or repositories; disclose them only to trusted recipients.

Risk: Declining an option notifies the contractor and changes the estimate's state.

Mitigation: Review the estimate and selected option before sending a decline; re-read the estimate afterward to confirm its status.

Risk: The skill includes unverified account, communications, media, and service-agreement endpoints beyond its stated purpose.

Mitigation: Do not probe those endpoints unless you explicitly intend that broader access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/housecallpro-mcp)
- [Housecall Pro customer portal recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers estimates and invoices; approvals must be completed in a browser.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
