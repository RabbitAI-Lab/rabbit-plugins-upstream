## Description:

Evaluate and improve code with Topos for complexity reduction, security checks, refactor verification, and PLATINUM/GOLD quality goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use this skill to measure and improve local repository structure, reduce complexity, verify refactors, and optimize toward Topos medal goals. It supports CLI and MCP-assisted code-quality loops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation relies on a remote shell installer and a global npm package.

Mitigation: Review the installer and npm package source before installation, and use CLI-only mode when MCP integration is not needed.

Risk: Running `topos install --all` can register MCP servers with supported agent harnesses.

Mitigation: Run MCP registration only when that integration is intentional, then verify the result with `topos status`.

Risk: Dependency graph generation can create `.gitnexus` artifacts and may involve project configuration side effects.

Mitigation: Run Topos in a Git repository, review generated artifacts before committing, and keep project configuration changes under normal code review.

Risk: Topos structural quality and SECURE signals are advisory and do not prove functional correctness or complete security.

Mitigation: Run project tests, linters, and dedicated security tooling before accepting refactors or treating SECURE results as sufficient assurance.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [CLI tables, ranked file lists, Markdown reports, shell commands, and MCP structured JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write .gitnexus graph artifacts when dependency graph generation is enabled; source files are changed only if the agent applies edits based on guidance.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter version is 0.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
