## Description:

Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). Use when creating persistent agents with AzureAIAgentsProvider, using hosted tools (code interpreter, file search, web search), integrating MCP servers, managing conversation threads, or implementing streaming responses. Covers function tools, structured outputs, and multi-tool agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thegovind](https://clawhub.ai/user/thegovind)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to create persistent Azure AI Foundry agents in Python, including hosted tools, MCP integrations, conversation threads, streaming responses, and structured outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pre-release package installation and hosted tool examples can change behavior or expand the remote execution surface.

Mitigation: Use an isolated, nonprivileged Python environment and pin reviewed package versions before adoption.

Risk: Hosted code, file search, web search, and MCP tools can expose prompts, uploaded files, credentials, or persistent thread identifiers to Azure or third-party services.

Mitigation: Treat Azure project credentials, MCP tokens, uploaded files, prompts, and thread IDs as sensitive, and do not send secrets, regulated data, or confidential documents unless data-handling requirements are satisfied.

Risk: MCP examples include automatic execution patterns and authenticated or private endpoints.

Mitigation: Require approvals or allowlist specific read-only tools before enabling MCP access, especially for private, authenticated, GitHub, or company API endpoints.

## Reference(s):

- [Agent Framework Azure AI Python Acceptance Criteria](references/acceptance-criteria.md)
- [Advanced Patterns Reference](references/advanced.md)
- [MCP Integration Reference](references/mcp.md)
- [Thread Management Reference](references/threads.md)
- [Hosted Tools Reference](references/tools.md)
- [Microsoft Agent Framework Repository](https://github.com/microsoft/agent-framework)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces implementation patterns for Azure AI Foundry agents; examples may involve hosted tools, MCP endpoints, uploaded files, and persistent thread IDs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
