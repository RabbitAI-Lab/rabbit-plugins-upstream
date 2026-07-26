## Description: <br>
Integrates the OpenAI Agents SDK with the You.com MCP server using Hosted MCP or Streamable HTTP in Python or TypeScript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardirby](https://clawhub.ai/user/edwardirby) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers use this skill to add You.com MCP-backed search and content tools to OpenAI Agents SDK projects. It guides language selection, MCP connection mode, package installation, environment variables, and new or existing integration files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated integration uses OpenAI and You.com API keys. <br>
Mitigation: Store keys in environment variables or a secret manager, avoid committing or logging them, and test first with non-sensitive prompts. <br>
Risk: Hosted MCP examples may allow automatic You.com tool execution. <br>
Mitigation: Review the generated tool configuration and approval posture before running it in a project or production workflow. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/edwardirby/skills/ydc-openai-agent-sdk-integration) <br>
- [OpenAI Agents SDK for Python](https://openai.github.io/openai-agents-python/) <br>
- [OpenAI Agents SDK for TypeScript](https://openai.github.io/openai-agents-js/) <br>
- [OpenAI Agents SDK MCP guide for Python](https://openai.github.io/openai-agents-python/mcp/) <br>
- [OpenAI Agents SDK MCP guide for TypeScript](https://openai.github.io/openai-agents-js/guides/mcp/) <br>
- [You.com MCP Server](https://documentation.you.com/developer-resources/mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python, TypeScript, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup steps, complete templates, integration snippets, environment variable guidance, validation checks, and troubleshooting notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
