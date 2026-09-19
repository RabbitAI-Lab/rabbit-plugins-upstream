## Description:

Read Housecall Pro customer estimate and invoice details from disposable portal links using shell commands, including totals, tax, contractor details, open options, invoice status, and the supported decline flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Housecall Pro customer-portal estimates or invoices from a shell, summarize amounts and contractor information, and handle the documented decline-only mutation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links are bearer credentials that can expose estimate or invoice data and authorize decline actions.

Mitigation: Keep links and tokens out of shared transcripts, logs, and commits; pass them through controlled variables or files.

Risk: Declining an estimate option sends an intentional customer response to the contractor and may not be reversible through this skill.

Mitigation: Read the estimate first, confirm the option id, run the decline command only intentionally, and re-read the estimate to verify the resulting status.

Risk: Estimate approval cannot be scripted because the portal requires an in-page reCAPTCHA token and approval is a binding commitment.

Mitigation: Open the Housecall Pro link in a browser and approve only through the portal UI.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on user-supplied Housecall Pro estimate or invoice links and tokens.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
