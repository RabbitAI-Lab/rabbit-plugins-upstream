## Description:

Helps agents read customer-facing Housecall Pro estimates and invoices with shell commands, and explains how to decline an estimate option safely.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and their agents use this skill to inspect contractor-sent estimates and invoices, summarize amounts owed, and optionally decline an estimate option without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anyone with a document link can read it or decline an estimate option.

Mitigation: Treat links and tokens as bearer credentials; keep them out of shared logs, transcripts, and commits.

Risk: Declining an option notifies the contractor that the customer is not proceeding.

Mitigation: Read the estimate and confirm the intended option before sending a decline request.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimate and invoice summaries require a valid document link; approvals must be completed in a browser.]

## Skill Version(s):

1.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
