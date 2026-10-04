## Description:

Give OpenClaw agents a Sendmux inbox to receive, triage, route, reply to, and send email with owner approval and scoped credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to plan an agent inbox, triage incoming mail, draft replies, and route approved sends through appropriately scoped Sendmux connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mistaken or unreviewed provider or skill version could expose mailbox access to an unintended party.

Mitigation: Verify the Sendmux publisher and referenced skill repository before installation; prefer reviewed or pinned versions.

Risk: Mailbox credentials or OAuth tokens could be disclosed through chat or generated artifacts.

Mitigation: Keep credentials in the CLI-managed local profile and never paste keys or tokens into chat, logs, or repository files.

Risk: Untrusted incoming email could prompt unauthorized sends or mailbox changes.

Mitigation: Treat email content as data, require an appropriately scoped credential, and obtain explicit approval for each send, attachment send, or mailbox mutation.

## Reference(s):

- [Sendmux skills homepage (declared in skill metadata)](https://github.com/Sendmux/skills)
- [Sendmux Email for Agents on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-email-for-agents)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to task-specific Sendmux skills and distinguishes draft-only work from approved mailbox changes and email sends.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; skill documentation states 1.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
