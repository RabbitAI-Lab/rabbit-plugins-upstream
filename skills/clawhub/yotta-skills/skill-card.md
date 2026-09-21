## Description:

元阁 yotta-skills routes agent skill needs, recommends YottaMeta skill combinations, and provides CLI and MCP-assisted workflows for listing, installing, updating, inventorying, and hook-checking yotta-* skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to select, install, update, inventory, and route among YottaMeta skill-family capabilities across supported agent environments. It is most useful when a user wants a reproducible installation plan, a local skill inventory, or guidance on which yotta-* skills to combine for a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can download, update, replace, and roll back files in agent skill directories.

Mitigation: Use an exact version or OpenClaw's audited install/update path in sensitive environments, run with --dry-run first, and target a specific --dir or --agent.

Risk: Global installation can place the installer into every known agent directory.

Mitigation: Avoid install.sh -g unless that broad placement is intentional and reviewed.

Risk: Unpinned npx execution can resolve a moving package version.

Mitigation: Prefer a pinned version or the default pinned manifest behavior when reproducibility matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [YottaMeta publisher profile](https://clawhub.ai/user/yottameta)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow](references/install-flow.md)
- [Skill list](references/skill-list.md)
- [Tutorial](references/tutorial.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown text with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose install, update, inventory, route, dry-run, rollback, and hook commands; user confirmation is expected before broad installation or configuration changes.]

## Skill Version(s):

0.19.14 (source: server release metadata, SKILL.md frontmatter, and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
