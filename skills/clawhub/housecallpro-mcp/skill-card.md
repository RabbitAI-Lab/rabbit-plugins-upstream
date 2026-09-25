## Description:

Reads Housecall Pro customer estimates and invoices from disposable customer portal links using curl, including totals, open options, company lookup, invoice status, and documented decline behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and interpret Housecall Pro customer estimate or invoice data from a supplied document link using shell commands. It helps agents summarize amounts, line items, tax, due balances, contractor details, and the limited decline workflow without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links are bearer credentials that may expose estimate or invoice data to anyone with the token.

Mitigation: Keep tokens out of shared transcripts, logs, commits, and pasted commands; store them only in controlled variables or local files.

Risk: The documented decline command can notify the contractor that the customer is not proceeding.

Mitigation: Read and verify the estimate first, run decline commands only when intended, and re-read the document afterward to confirm the resulting status.

Risk: Attempting to script approval could bypass the intended browser confirmation flow for a binding commitment.

Mitigation: Do not script approval; use the browser approval flow when the customer intends to approve an estimate.

## Reference(s):

- [Housecall Pro consumer API recipes](artifact/references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code]

**Output Format:** [Markdown with shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce curl commands and jq filters that read JSON estimate or invoice responses; decline commands perform a state-changing action.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
