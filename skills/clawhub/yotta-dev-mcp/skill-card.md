## Description:

A local MCP development toolkit for mapping repositories, reviewing architecture and changes, checking dependencies and secrets, and recording verification evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect codebases, assess architectural and change impacts, review code, and collect evidence for checks and releases. Most operations are read-only; execution and file changes require explicit opt-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Host diagnostics may inspect local agent and MCP configuration locations and installed skill metadata.

Mitigation: Invoke mcp_doctor only when host-configuration inspection is intended.

Risk: Explicit execution or apply modes can run checks or write project files.

Mitigation: Leave allow_execute and apply disabled unless the requested checks or file changes are intended.

Risk: An unpinned installation may differ from the reviewed release.

Mitigation: Pin installation to the reviewed 0.2.2 release where possible.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Project homepage (release listing)](https://github.com/YottaMeta/yotta-dev-mcp)
- [Tool reference](references/tools.md)
- [Architecture contract](references/architecture-contract.md)
- [Adapter reference](references/adapters.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [JSON tool results and human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include file and line evidence; unresolved checks are reported as UNKNOWN.]

## Skill Version(s):

0.2.2 (source: ClawHub release, skill frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
