## Description:

Golang semantic code intelligence via `gopls`, the official Go language server for navigation, references, call and implementation hierarchy, workspace symbol search, package API discovery, diagnostics, safe rename, refactors, formatting, and generated tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to apply semantic Go language-server intelligence while navigating, understanding, diagnosing, formatting, testing, and safely refactoring Go workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local Go project files, resolve dependencies, and write code changes when refactoring or formatting is requested.

Mitigation: Review proposed edits and diagnostics before accepting changes, and run targeted Go tests for changed packages.

Risk: Optional setup steps may modify local MCP or LSP configuration.

Mitigation: Apply integration commands only in the intended agent or editor environment and confirm the resulting configuration.

## Reference(s):

- [gopls MCP server and native LSP tool reference](references/mcp.md)
- [gopls CLI reference](references/cli.md)
- [gopls feature catalog](references/features.md)
- [Capability to CLI, MCP, and native LSP matrix](references/matrix.md)
- [gopls settings reference](references/settings.md)
- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-gopls)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Upstream gopls features](https://tip.golang.org/gopls/features/)
- [Upstream gopls settings](https://tip.golang.org/gopls/settings)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline tool calls, file references, shell commands, and code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in the locally resolved Go workspace and depend on available gopls, MCP, LSP, or CLI integrations.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
