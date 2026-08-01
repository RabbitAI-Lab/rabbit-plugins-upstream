## Description: <br>
Use when turning supplied API sources into a safe TypeMCP project. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sjungwon03](https://clawhub.ai/user/sjungwon03) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert supplied local OpenAPI, Swagger UI, Markdown, or HTML API references into a TypeMCP stdio project with manifest review, generation approval, and optional agent installation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local code generation plus optional generated-project verification can install npm dependencies and run local build or test commands. <br>
Mitigation: Use a fresh empty output directory and run npm verification in a container, VM, or equivalent host sandbox when dependencies are untrusted. <br>
Risk: Optional MCP agent installation can modify local agent configuration files. <br>
Mitigation: Keep project-only unless agent installation is explicitly needed, and review every config path, command, argument, environment-variable name, and backup path before approving installation. <br>
Risk: Generated API tools may include mutating operations. <br>
Mitigation: Leave protected operations disabled unless exact operation IDs are explicitly approved before request construction. <br>


## Reference(s): <br>
- [TypeMCP Runtime Contract](references/type-mcp-runtime.md) <br>
- [Agent MCP Installation Reference](references/agent-mcp-installation.md) <br>
- [Hermes MCP Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) <br>
- [Claude Code MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp) <br>
- [Codex CLI Reference](https://developers.openai.com/codex/cli/reference) <br>
- [Cursor MCP Documentation](https://cursor.com/docs/mcp) <br>
- [VS Code MCP Servers Documentation](https://code.visualstudio.com/docs/agent-customization/mcp-servers) <br>
- [Gemini CLI MCP Server Documentation](https://geminicli.com/docs/tools/mcp-server/) <br>
- [OpenCode MCP Servers Documentation](https://opencode.ai/docs/mcp-servers/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with generated TypeScript project files, JSON manifests, and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generation is gated by manifest review and single-use approval; optional agent installation uses a separate reviewed plan.] <br>

## Skill Version(s): <br>
0.2.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
