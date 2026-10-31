## Description:

元开 provides 18 deterministic local development tools through a stdio MCP server for code mapping, architecture and change review, verification, security checks, and workflow support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the MCP tools to understand unfamiliar codebases, review architecture and change impact, verify changes, inspect code, scan for secrets or dependency issues, and manage development workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may delete or overwrite files outside its intended folder.

Mitigation: Wait for installer path safeguards before using it; prefer the reviewed local Python launcher over unpinned npx commands.

Risk: Some checks may run programs, and Git-based checks on untrusted repositories need additional safeguards.

Mitigation: Enable execution only for trusted projects and avoid Git-based checks on untrusted repositories until text-conversion helpers are disabled.

Risk: Diagnostics may inspect paths beyond the intended configuration and skill files.

Mitigation: Limit diagnostics to the intended configuration and skill paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-dev-mcp)
- [Project homepage](https://github.com/YottaMeta/yotta-dev-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Structured tool results and reports, with code or shell examples where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include file and line evidence; behavior is deterministic and offline by default, with writes and command execution controlled by explicit options.]

## Skill Version(s):

0.2.5 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
