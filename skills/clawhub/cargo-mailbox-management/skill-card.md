## Description:

Guides agents through Cargo CLI workflows for provisioning and warming Cargo-owned sending mailboxes, checking send allowance and suppression status, sending email, and reading threads, replies, delivery events, pricing, and troubleshooting signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo-owned sending inboxes: provision mailboxes, warm them up, check daily allowance and suppression state, send from approved mailboxes, and inspect replies, events, errors, and recurring mailbox costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live email sends with no CLI dry run.

Mitigation: Confirm recipient permission, suppression status, relevance, mailbox status, and daily allowance before sending; send to yourself first when the rendered message needs review.

Risk: Provisioning mailboxes creates recurring monthly credit charges.

Mitigation: Read live pricing and existing mailbox count, quote the recurring monthly cost, and require explicit approval before provisioning.

Risk: Suppressed recipients or unqualified audiences could be contacted if checks are skipped.

Mitigation: Treat basis, suppression, and relevance as blocking pre-send checks, and remove suppressed recipients from the audience rather than trying to bypass suppression.

Risk: Operational limits can be misread, leading to failed sends or misleading reporting.

Mitigation: Use get-send-allowance before batch enrollment, distinguish allowance from warm-up stats, and do not treat empty bounce data as proof of deliverability.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Warm-up and the send ramp](references/warmup-and-allowance.md)
- [Sending: the sendEmail action](references/sending.md)
- [Response shapes and enums](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Mailbox recipes](references/examples/recipes.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with CLI command examples and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires @cargo-ai/cli and an authenticated Cargo workspace; guided commands can create recurring mailbox charges and send live email.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
