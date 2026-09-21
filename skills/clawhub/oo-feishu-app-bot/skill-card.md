## Description:

Feishu App Bot helps agents read, create, update, and delete Feishu/Lark resources through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage Feishu/Lark messages, Drive, Wiki, Docs, Sheets, Slides, Base, calendars, tasks, OKRs, mail, and slash commands through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write, overwrite, or delete Feishu/Lark data through many actions.

Mitigation: Confirm the exact target, payload, and expected effect before write actions, and require explicit approval before destructive actions.

Risk: The setup guidance includes running a remote installer directly in a shell.

Mitigation: Prefer a trusted or manual oo CLI installation path and review the installer source before execution.

Risk: Connected Feishu app scopes and workspaces determine what data the agent can access or change.

Mitigation: Review requested scopes and connect only the workspaces and accounts the agent is intended to manage.

## Reference(s):

- [Feishu App Bot homepage](https://open.feishu.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.6 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
