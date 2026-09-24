## Description:

Read Housecall Pro customer estimates and invoices from document links with plain curl, summarize amounts and line items, and explain why approval must be completed in a browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Housecall Pro customers and developers use this skill to retrieve estimate or invoice details from document links, summarize totals and line items, and understand the limited shell-supported actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links and tokens act as bearer credentials.

Mitigation: Keep links and tokens out of shared transcripts, logs, and commits; store them only in local variables or files you control.

Risk: The skill includes a real decline action that can notify the contractor that the customer is not proceeding.

Mitigation: Read the estimate first, confirm the selected option id, and re-read the document after any decline request to verify the result.

Risk: The artifact lists unverified portal endpoints beyond the documented estimate and invoice flows.

Mitigation: Use the verified read and decline examples for normal workflows, and avoid unverified endpoints unless deliberately investigating broader portal behavior.

Risk: Approval cannot be safely scripted because the portal requires an in-page reCAPTCHA token.

Mitigation: Complete approval in the browser and do not attempt to bypass the portal's approval flow.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON/jq processing snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes warnings for bearer-token handling, decline behavior, and browser-only approval.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
