## Description:

Let an OpenClaw agent read, search, count, sync, triage, file, delete, thread, and reply from one Sendmux mailbox efficiently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an OpenClaw agent work with a single Sendmux mailbox for search, triage, sync, filing, deletion, threading, replies, and attachment-aware workflows while preserving explicit approval boundaries for risky actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables mailbox-scoped email access and may expose sensitive message content if credentials or mailbox data are mishandled.

Mitigation: Use a mailbox-scoped key, scoped agent token, or mailbox-limited OAuth grant rather than a root key, and do not ask users to paste secrets into chat.

Risk: An agent could mutate, delete, move, label, or send email without sufficient user intent.

Mitigation: Review proposed send, delete, label, move, and other mutation actions before approval, and require explicit confirmation for destructive or send-capable operations.

Risk: Inbound email bodies, headers, links, and attachments can contain untrusted instructions.

Mitigation: Treat mailbox content as untrusted data and do not let message content drive credential disclosure, skill installation, configuration changes, or sending actions.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mailbox-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell, TypeScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes mailbox-scoped credential handling, confirmation requirements for mutation and send actions, and routing to related Sendmux skills.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
