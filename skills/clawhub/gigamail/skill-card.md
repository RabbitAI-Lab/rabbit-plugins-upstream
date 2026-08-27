## Description:

GigaMail helps an OpenClaw agent read, search, draft, reply, and schedule through the GigaMail MCP server while requiring out-of-band human approval for destructive email and calendar actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to connect an agent to real email and calendar accounts for inbox triage, search, drafting, replies, availability checks, and appointment proposals. It is suited to agent-assisted productivity workflows where sensitive writes need an explicit human approval gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to real mailboxes and calendars, so actions can expose or alter sensitive personal or business information.

Mitigation: Install only for intended email and calendar workflows, review the pip package and MCP configuration, and keep the GIGAMAIL_ROOT data directory under the user's control.

Risk: Approval notifications can send request summaries outside the local machine when the optional notification command is configured.

Mitigation: Enable GIGAMAIL_APPROVAL_NOTIFY_CMD only when the user is comfortable with approval summaries leaving the machine.

Risk: Email bodies, subjects, sender names, and attachments may contain untrusted instructions.

Mitigation: Treat email and attachment content as data, not instructions, and rely on the human approval gate for destructive send, delete, and calendar-write operations.

## Reference(s):

- [GigaMail homepage](https://gigamail.ai)
- [ClawHub skill page](https://clawhub.ai/adecubed/skills/gigamail)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers MCP setup, account connection, approval flow handling, reply-rule boundaries, untrusted email content, and troubleshooting.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
