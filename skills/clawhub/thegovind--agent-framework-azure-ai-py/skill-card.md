## Description: <br>
Build Azure AI Foundry agents using the Microsoft Agent Framework Python SDK (agent-framework-azure-ai). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create persistent Azure AI Foundry agents in Python with AzureAIAgentsProvider, hosted tools, MCP integrations, conversation threads, streaming responses, and structured outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples can connect agents to Azure, Bing web search, file search, code execution, and MCP services that may process sensitive prompts or files. <br>
Mitigation: Use least-privilege Azure and MCP credentials, avoid hardcoded tokens, and review data handling before sending prompts or uploading private files. <br>
Risk: Hosted tools and MCP actions can perform powerful operations when copied into real projects. <br>
Mitigation: Require approval for sensitive or mutating MCP actions and review tool configuration before deployment. <br>
Risk: Unpinned package installation examples may resolve to changing prerelease package versions. <br>
Mitigation: Pin package versions before using examples in production projects. <br>


## Reference(s): <br>
- [Hosted Tools Reference](references/tools.md) <br>
- [MCP Integration Reference](references/mcp.md) <br>
- [Thread Management Reference](references/threads.md) <br>
- [Advanced Patterns Reference](references/advanced.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Microsoft Agent Framework Repository](https://github.com/microsoft/agent-framework) <br>
- [ClawHub Skill Page](https://clawhub.ai/thegovind/skills/agent-framework-azure-ai-py) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include Azure configuration values, package installation commands, SDK usage patterns, and review criteria.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
