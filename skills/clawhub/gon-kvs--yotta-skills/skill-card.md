## Description:

Yotta Skills helps agents inventory installed skills, route tasks to YottaMeta skill combinations, and generate install or update commands for selected skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gon-kvs](https://clawhub.ai/user/gon-kvs)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to plan which YottaMeta skills fit a task, inspect local skill inventories, and prepare installation or update commands for a target agent or directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download, install, update, and replace skills in agent directories.

Mitigation: Require explicit user confirmation before every install or update, prefer dry-run previews, and scan skills before installation.

Risk: The skill describes persistent agent-behavior changes through memory-file updates and MCP configuration edits.

Mitigation: Require explicit approval before memory-file or MCP configuration changes, and review the exact file edits before applying them.

Risk: The release security summary flags conflicting auto-install instructions.

Mitigation: Treat routing and installation output as recommendations only; do not auto-install missing skills or auto-run high-risk actions without user confirmation.

Risk: Global install behavior can copy the installer across many agents.

Mitigation: Avoid the global install.sh mode unless broad installation across agents is intentional.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gon-kvs/skills/yotta-skills)
- [NPM package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Skill list](references/skill-list.md)
- [Install flow](references/install-flow.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text, shell command snippets, and optional JSON responses from CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose installs, updates, MCP configuration edits, inventory scans, and routing steps; user confirmation is expected before filesystem or configuration changes.]

## Skill Version(s):

0.5.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
