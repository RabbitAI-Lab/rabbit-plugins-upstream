## Description:

Guides agents through Cargo mailbox provisioning, warm-up, send allowance checks, live send execution, reply and event review, suppression handling, and mailbox pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting Cargo users use this skill to manage real sending inboxes, warm-up state, allowances, sends, replies, delivery events, suppressions, and mailbox costs through the Cargo CLI. It is intended for operators who need guarded mailbox workflows rather than copywriting or audience-building guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Cargo CLI use can manage real sending inboxes and make persistent mailbox or suppression changes.

Mitigation: Install and use the skill only when the operator intends to manage Cargo mailboxes; confirm the active workspace before write actions.

Risk: CLI sends are live and can contact real recipients.

Mitigation: Check basis, suppression, relevance, and send allowance before sending, and send to a controlled recipient first when validating a workflow.

Risk: Mailbox provisioning can create recurring monthly credit charges.

Mitigation: Review live pricing and fleet size before provisioning, and remove unused mailboxes to stop recurring charges.

## Reference(s):

- [Cargo mailbox-management ClawHub page](https://clawhub.ai/cargo-ai/skills/cargo-mailbox-management)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Mailbox recipes](references/examples/recipes.md)
- [Response shapes and enums](references/response-shapes.md)
- [Sending: the sendEmail action](references/sending.md)
- [Troubleshooting](references/troubleshooting.md)
- [Warm-up and the send ramp](references/warmup-and-allowance.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concise tables or summaries instead of raw command output.]

## Skill Version(s):

1.0.2 (source: frontmatter, artifact metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
