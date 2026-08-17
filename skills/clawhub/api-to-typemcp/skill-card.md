## Description:

Use when turning supplied API sources into a safe TypeMCP project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sjungwon03](https://clawhub.ai/user/sjungwon03)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert supplied local OpenAPI or Swagger specs, Swagger UI HTML, or Markdown/HTML API references into a TypeMCP stdio project. It supports manifest review, digest-bound approval, contained verification, and optional agent installation after separate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional agent installation can modify local agent configuration.

Mitigation: Review the exact secret-free installation plan, including target paths, command, arguments, working directory, environment variable names, and backup paths, before issuing the separate plan-bound confirmation.

Risk: Generated-project verification installs npm dependencies and runs build and smoke-test commands.

Mitigation: Inspect the generated package and lockfile, use npm ci with lifecycle scripts disabled as documented, and run verification in a container, VM, or equivalent host sandbox when the project or dependency graph is untrusted.

Risk: The inspected release appears unable to generate because a required template file is missing.

Mitigation: Verify the package has been fixed and generation succeeds before relying on this release for production work.

Risk: Generated MCP tools may expose mutating API operations if they are approved too broadly.

Mitigation: Keep protected operations denied by default and allow only exact reviewed operation IDs through TYPE_MCP_ALLOW_PROTECTED_OPERATIONS before request construction or dispatch.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sjungwon03/skills/api-to-typemcp)
- [TypeMCP Runtime Contract](references/type-mcp-runtime.md)
- [Agent MCP Installation Reference](references/agent-mcp-installation.md)
- [Hermes MCP Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Claude Code MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [Codex CLI Reference](https://developers.openai.com/codex/cli/reference)
- [Cursor MCP Documentation](https://cursor.com/docs/mcp)
- [VS Code MCP Servers Documentation](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON manifests, shell commands, and generated TypeScript/Node project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation is gated by a reviewed manifest digest and a single-use approval receipt; optional agent installation uses a separate reviewed plan and confirmation.]

## Skill Version(s):

0.2.6 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
