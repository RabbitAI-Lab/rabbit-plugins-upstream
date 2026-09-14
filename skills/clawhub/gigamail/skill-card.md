## Description:

GigaMail lets an OpenClaw agent read, search, draft, reply, schedule, and request approved email or calendar changes through the GigaMail MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to connect an agent to real Microsoft 365 or IMAP mailboxes and calendars for inbox triage, attachment reading, reply drafting, availability checks, and appointment proposals while retaining human approval for destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and configuring the skill gives the GigaMail MCP server access to real mailbox and calendar data.

Mitigation: Use a reviewed version, keep the server isolated from unrelated files and credentials, and review approval prompts before allowing sends, deletes, or calendar changes.

Risk: The documented pip install is unpinned, so a future install may resolve to a different server version than the reviewed release.

Mitigation: Install a specific reviewed GigaMail package version when reproducibility or change control matters.

Risk: Email bodies, sender names, subjects, and attachment text can contain untrusted instructions.

Mitigation: Treat mailbox and attachment content as data, not agent instructions, and ask the user before acting on sensitive requests found in messages.

## Reference(s):

- [GigaMail ClawHub Skill Page](https://clawhub.ai/adecubed/skills/gigamail)
- [adecubed ClawHub Publisher Profile](https://clawhub.ai/user/adecubed)
- [GigaMail Homepage](https://gigamail.ai)
- [Source Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dangerous email and calendar actions require out-of-band human approval before execution.]

## Skill Version(s):

0.3.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
