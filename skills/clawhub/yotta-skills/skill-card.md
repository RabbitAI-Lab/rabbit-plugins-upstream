## Description:

元阁 yotta-skills helps an agent list, route, install, update, and inventory YottaMeta skill-family packages through CLI guidance, optional MCP routing, and local registry scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose YottaMeta skill combinations for a task, preview or install selected skills, update existing installations, and inventory locally installed skills. It is useful when maintaining a skill collection across supported agent clients or routing a task to an appropriate YottaMeta skill bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download YottaMeta skills, replace existing skill directories, and maintain a local registry.

Mitigation: Use --dry-run and --pin first, choose an explicit --dir or supported --agent target, and back up customized skills before install or update.

Risk: The skill asks the agent to change persistent memory files and optional MCP configuration.

Mitigation: Do not permit writes to AGENTS.md, CLAUDE.md, mcpServers, or equivalent persistent configuration unless the user explicitly approves the exact change.

Risk: The skill may encourage automatic installation or application of skills even though routing is advisory.

Mitigation: Treat route results as recommendations; require explicit user approval before installing missing skills or enabling automatic use behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Orchestration Decision Table](references/orchestration.md)
- [Install Flow](references/install-flow.md)
- [Skill List](references/skill-list.md)
- [Chinese Tutorial](references/tutorial.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI and MCP workflows can return text summaries or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include routing candidates, call order, confidence, installed or missing status, install commands, inventory data, and installation or update summaries.]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata; artifact frontmatter and package.json report 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
