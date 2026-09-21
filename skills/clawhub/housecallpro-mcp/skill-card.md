## Description:

Read Housecall Pro customer estimates and invoices from the shell with curl and jq, including totals, line items, contractor details, and the decline workflow while explaining why approval must happen in the browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Housecall Pro customer portal estimate or invoice links they received, extract money fields and contractor details, and understand which actions can be safely handled from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links act as bearer credentials that can expose estimate or invoice data.

Mitigation: Keep tokens and downloaded JSON files out of shared transcripts, logs, and repositories, and use variables or local files under the user's control.

Risk: The skill includes a ready-to-run command that can decline a real contractor estimate and notify the contractor.

Mitigation: Review the exact option identifier and intended outcome before running any decline command, then re-read the estimate to confirm the resulting status.

Risk: A shell client cannot approve an estimate because approval requires an in-page reCAPTCHA response token.

Mitigation: Handle approvals only in the browser flow and do not attempt to bypass the documented approval control.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown with inline shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl requests that read customer portal JSON and a POST command to decline an estimate option.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
