## Description:

Provides local, deterministic developer tools for codebase mapping, architecture and change-impact review, verification, code review, and release checks through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect repositories, assess architecture and change impact, review code, and collect evidence for verification and release decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can write to multiple agent directories.

Mitigation: Use a reviewed or pinned package version and dry-run or select a single target directory unless broad installation is intended.

Risk: Local diagnostics and secret scans can inspect sensitive files and configuration.

Mitigation: Run mcp_doctor and scan_secrets only against local files you are authorized to inspect.

Risk: Explicit execution or apply options can run local checks or write files.

Mitigation: Review the target and commands before enabling allow_execute=true or apply=true; leave the default read-only mode in place otherwise.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-dev-mcp)
- [Architecture contract reference](references/architecture-contract.md)
- [Tool reference](references/tools.md)
- [Optional adapters reference](references/adapters.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands, Configuration]

**Output Format:** [Structured JSON tool results and agent-facing text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include file, line, rule, and evidence when available; missing evidence is reported as UNKNOWN.]

## Skill Version(s):

0.2.3 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
