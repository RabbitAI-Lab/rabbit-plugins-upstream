## Description:

A local stdio MCP server that gives development agents deterministic tools for repository mapping, architecture and change analysis, verification, code review, and security scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers use the MCP server to map an unfamiliar codebase, assess architecture and change impact, review code, and gather verification evidence. They can also run optional checks and adapters when explicitly enabled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow reads may expose private files outside the selected project when links escape the project boundary.

Mitigation: Use the core tool profile or filesystem isolation until workflow reads reject links that escape the project.

Risk: Enabling tests or adapters can execute code, and npx may download and execute a package.

Mitigation: Enable tests and adapters only for trusted code; prefer reviewed local Python scripts or an exact npm version, and account for npx downloads.

Risk: Configuration diagnostics may inspect more local configuration than needed.

Mitigation: Supply both config_paths and skills_dirs to limit diagnostic scope.

Risk: An empty Git-history scan may be incomplete.

Mitigation: Independently verify Git-history scanning before relying on an empty result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Project homepage](https://github.com/YottaMeta/yotta-dev-mcp)
- [Architecture contract](references/architecture-contract.md)
- [Tool reference](references/tools.md)
- [Adapter reference](references/adapters.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured JSON tool results with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include file and line evidence where applicable; command execution and writes require explicit flags.]

## Skill Version(s):

0.2.6 (source: server release, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
