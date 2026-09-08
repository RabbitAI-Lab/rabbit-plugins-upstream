## Description:

GigaMail lets an OpenClaw agent read, search, draft, reply, and schedule through a local email and calendar MCP server while requiring out-of-band human approval for send, delete, and calendar write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use GigaMail to let an agent triage inboxes, search messages and attachments, draft replies, and work with calendars while keeping destructive actions behind human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuring the skill gives the local MCP server access to real email and calendar data.

Mitigation: Install a trusted GigaMail release, review the upstream package before use, and configure only accounts and knowledge files the user is comfortable exposing to the local server.

Risk: The release installs an external Python package without a pinned version in the skill instructions.

Mitigation: Prefer installing a specific trusted GigaMail package version and review release provenance before deployment.

Risk: Read access remains sensitive even though destructive actions require human approval.

Mitigation: Treat mailbox contents, calendar data, attachments, identity files, and knowledge files as private data and limit configured accounts to the intended use case.

## Reference(s):

- [GigaMail homepage](https://gigamail.ai)
- [ClawHub GigaMail skill](https://clawhub.ai/adecubed/skills/gigamail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers MCP tool use, setup commands, and human approval workflow boundaries.]

## Skill Version(s):

0.3.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
