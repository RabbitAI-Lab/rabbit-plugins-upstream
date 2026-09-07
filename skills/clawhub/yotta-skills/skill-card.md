## Description:

YuanGe (yotta-skills) provides orchestration routing, local skill inventory, and one-command installation or update workflows for the YottaMeta skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose YottaMeta skill combinations, inspect installed skills, and install or update selected yotta-* skills into an agent or target directory. It is most relevant when an agent needs a repeatable way to route a task to supporting skills, preview changes, or maintain a local skill registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update remote skills and may make broad changes when global targets or automatic update modes are used.

Mitigation: Review before installing, use explicit target directories, prefer pinned versions, and avoid global or automatic update modes unless broad changes are intended.

Risk: The skill text asks agents to add persistent session-start behavior to agent memory or configuration files.

Mitigation: Do not allow automatic writes to AGENTS.md, CLAUDE.md, or MCP server configuration without explicit user review and approval.

Risk: Scanner evidence marks the release as suspicious because installer and router behavior has weak guardrails around remote skill changes.

Mitigation: Treat scanner warnings as a stop-and-inspect signal, scan downloaded skills before use, and confirm update or install plans before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)
- [Skill list](references/skill-list.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown or plain text guidance with shell commands, plus optional JSON output from CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include install plans, route recommendations, inventory summaries, update reports, and target-directory configuration snippets.]

## Skill Version(s):

0.6.2 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
