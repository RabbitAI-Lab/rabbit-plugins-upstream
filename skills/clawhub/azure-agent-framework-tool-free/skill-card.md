## Description: <br>
Guides developers using the Microsoft Agent Framework Python SDK to build persistent Azure AI Foundry agents with function tools, hosted tools, streaming responses, session threads, and structured output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill for guidance and examples when creating Azure AI Foundry agents, wiring Python function tools, using hosted tools, streaming responses, managing conversation threads, and configuring structured outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Following the examples may install packages, change environment variables, authenticate with Azure CLI, or create hosted agents and tools that use Azure resources or credentials. <br>
Mitigation: Approve package installs, Azure CLI login, environment changes, and any Azure AI Foundry resource creation before allowing an agent to execute commands. <br>
Risk: Hosted tools such as code interpreter, file search, web search, and MCP integrations can act on data or services connected to the Azure project. <br>
Mitigation: Use least-privilege credentials, review tool and connection settings, and run examples in a controlled Azure project before broader use. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Azure CLI authentication, Azure AI Foundry project settings, model deployment environment variables, and approval before cloud or credential changes.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
