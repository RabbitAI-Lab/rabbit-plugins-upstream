## Description:

元阁 yotta-skills helps agents plan YottaMeta skill combinations, route requests, install or update selected yotta-* skills, inventory local skills, and evaluate hook support with user-confirmed changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to select YottaMeta skill combinations, generate routing guidance, inventory installed skills, and prepare explicit install or update commands before changing an agent environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add, replace, roll back, and inventory files in agent skill directories.

Mitigation: Start with `--dry-run`, review the planned target directory and skill list, and prefer host-native install or update flows where available.

Risk: Mutable npm execution and broad self-install behavior can change what code is fetched or installed.

Mitigation: Use exact-version commands or pinned releases, review the package source and release hash, and avoid `install.sh -g/--global` unless that scope is explicitly intended.

Risk: Optional MCP configuration or global memory writes can persist behavior beyond the current session.

Mitigation: Approve those writes only after reviewing the target path and full text or configuration that will be written.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Homepage from ClawHub metadata](https://github.com/YottaMeta/yotta-skills)
- [元阁编排策划](references/orchestration.md)
- [安装器工作原理](references/install-flow.md)
- [全家技能清单](references/skill-list.md)
- [元阁常见问题](references/faq.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown text with CLI commands and optional JSON output from CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include install, update, inventory, route, rollback, and hook evaluation commands; configuration and global memory writes require explicit user confirmation.]

## Skill Version(s):

0.19.17 (source: server release, frontmatter, package.json, skill-manifest.json, CHANGELOG v0.19.17 released 2026-09-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
