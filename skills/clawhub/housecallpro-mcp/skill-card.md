## Description:

Guides customers in reading Housecall Pro estimates and invoices from the shell and declining estimate options without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and developers use this skill to inspect contractor estimates, line items, invoice totals, and amounts due with shell commands. It also explains how to decline an estimate option and why approvals must happen in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer links grant access to the document and can authorize a decline if disclosed.

Mitigation: Keep links and tokens out of shared logs, transcripts, and repositories; store them only in a controlled variable or file.

Risk: Declining an option can notify the contractor and may not be reversible from the shell.

Mitigation: Review the estimate and selected option before declining, then re-read the document to confirm its status.

Risk: An approval commits the customer to a quoted price and cannot be scripted with this skill.

Mitigation: Complete approvals in the browser; do not attempt to bypass the approval flow.

## Reference(s):

- [Housecall Pro consumer API recipes](artifact/references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries of estimates or invoices may include customer and contractor details; amounts are reported in currency units rather than integer cents.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
