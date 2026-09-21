## Description:

Notion (notion.so). Use this skill for ANY Notion request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to search, read, create, update, and delete Notion workspace content through an OOMOL-connected Notion account. It is intended for workflows that need live Notion data access with schema inspection before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs the agent to execute remote installer scripts, which the security evidence flags as suspicious.

Mitigation: Review the installer path before installing, prefer a verified package or signed release, and avoid running remote installer commands unless the user explicitly approves.

Risk: The skill can create, update, overwrite, archive, or delete Notion content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any action tagged write or destructive.

Risk: Connecting Notion grants the skill access to workspace data through OOMOL-managed credentials.

Mitigation: Connect only Notion workspaces and scopes where read, write, and destructive actions are acceptable after explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-notion)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Notion homepage](https://www.notion.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI actions that return JSON responses and may modify Notion workspace state after confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
