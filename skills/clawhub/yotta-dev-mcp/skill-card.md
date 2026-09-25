## Description:

A local MCP toolkit that helps developers map repositories, review architecture and code changes, assess impact, and run evidence-based checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this local MCP server to understand unfamiliar codebases, assess architecture and change impact, review findings, and verify releases with traceable evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floating npx installation may run a different release from the reviewed version.

Mitigation: Pin the reviewed version, such as @yottameta/yotta-dev-mcp@0.2.0.

Risk: Explicitly enabled checks or apply actions may execute local commands or write files.

Mitigation: Enable allow_execute=true or apply=true only for intended actions after reviewing their scope.

Risk: MCP diagnostics may inspect default user-level skill and configuration locations.

Mitigation: Supply explicit mcp_doctor paths when default locations should not be inspected.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Project homepage (listed in metadata)](https://github.com/YottaMeta/yotta-dev-mcp)
- [Tool reference](references/tools.md)
- [Architecture contract reference](references/architecture-contract.md)
- [Optional adapter reference](references/adapters.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Configuration, Shell commands]

**Output Format:** [Structured JSON tool responses and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked findings and explicit unknowns; local execution and writes require opt-in.]

## Skill Version(s):

0.2.0 (source: skill frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
