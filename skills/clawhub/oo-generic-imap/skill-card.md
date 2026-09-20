## Description:

Enables agents to operate a connected generic IMAP mailbox through OOMOL's oo CLI for reading, searching, sending, replying, forwarding, and mailbox state changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent interact with a connected IMAP mailbox: list folders, inspect and search messages, fetch parsed email content, download attachments, and perform confirmed send or mailbox-state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email-changing operations can alter or remove mailbox data.

Mitigation: Confirm exact targets and payloads before sending, moving, marking, or deleting emails.

Risk: Setup may involve installing the oo CLI from a downloaded script.

Mitigation: Use a verified installation method before allowing the skill to operate a connected mailbox.

## Reference(s):

- [IMAP RFC 3501](https://www.rfc-editor.org/rfc/rfc3501)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-generic-imap)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
