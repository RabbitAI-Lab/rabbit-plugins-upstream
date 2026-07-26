## Description: <br>
Build AI agents using the Azure AI Agents Python SDK for Azure AI Foundry, including tools, threads, messages, streaming responses, and vector stores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to draft and review Python SDK code and configuration for Azure AI Foundry agents, including tools, threads, streaming, vector stores, and async workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copyable examples could let agent-provided text run local code if used as written. <br>
Mitigation: Do not copy the eval-based calculator pattern; replace it with a restricted math parser or explicit validated operations. <br>
Risk: Examples use hosted Azure tools and external tool connectors that may process sensitive data or call untrusted resources. <br>
Mitigation: Use least-privilege Azure credentials, avoid sending secrets or regulated data to hosted tools, and connect only trusted MCP, OpenAPI, Bing, and Azure Function resources. <br>
Risk: Example agents, files, vector stores, or queues may persist after experimentation. <br>
Mitigation: Clean up agents, files, vector stores, and queues after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-ai-agents-py) <br>
- [Azure AI Agents SDK Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Tools Reference](references/tools.md) <br>
- [Streaming Reference](references/streaming.md) <br>
- [Async Patterns Reference](references/async-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SDK import patterns, Azure environment variables, tool setup examples, streaming handlers, async workflows, and cleanup guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
