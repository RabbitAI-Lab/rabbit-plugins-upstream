## Description:

Reads Housecall Pro customer estimates and invoices from contractor portal links with shell curl commands, covering line items, totals, taxes, balances, contractor details, option decline workflow, and why approval cannot be scripted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Housecall Pro estimate or invoice links from the shell without installing the MCP server. It helps summarize document data, check whether estimate options are open, and perform a clearly disclosed decline action when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links are bearer credentials that can expose customer estimate or invoice data and may permit decline actions.

Mitigation: Keep tokens and saved JSON private, avoid shared transcripts and logs, and never commit document links or retrieved data.

Risk: Declining an estimate option may not be reversible from the shell and informs the contractor that the option is not proceeding.

Mitigation: Read the estimate first, verify the exact option identifier, run the decline command only for the intended option, and re-read the estimate to confirm status.

Risk: Approval is a binding commitment and cannot be safely scripted by this skill because it requires an in-page reCAPTCHA token.

Mitigation: Use the Housecall Pro browser flow for approval and do not attempt to bypass the page action.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with inline shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-facing instructions and command snippets; commands may save estimate or invoice JSON locally.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
