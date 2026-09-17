## Description:

Notion (notion.so). Use this skill for ANY Notion request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, search, create, update, move, and delete Notion pages, blocks, databases, data sources, users, and page content through an OOMOL-connected Notion account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute unverified code during first-time setup.

Mitigation: Install the oo CLI through a trusted process with source verification and version pinning instead of allowing an agent to run remote install commands automatically.

Risk: Write and destructive Notion actions can modify, move, archive, or overwrite workspace content.

Mitigation: Confirm the exact action, target identifiers, and JSON payload with the user before running any write or destructive command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-notion)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Notion](https://www.notion.so)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Notion connector command payloads and summarize JSON responses from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
