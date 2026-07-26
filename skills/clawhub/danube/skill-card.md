## Description: <br>
Connect your AI agent to a growing marketplace of services and tools through a single API key, with guidance to discover, search, and execute available Danube tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[preston-thiele](https://clawhub.ai/user/preston-thiele) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an agent to Danube, configure the MCP server, discover available marketplace services, and execute tools after gathering required parameters and credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Danube API key can enable broad third-party tool execution and user-scoped write actions through a single credential. <br>
Mitigation: Require explicit user approval before writes, deletions, messages, purchases, credentialed service actions, workflow or skill changes, and batch executions. <br>
Risk: Tool parameters may send sensitive data to connected third-party services. <br>
Mitigation: Connect only the accounts needed for the task and avoid sending unnecessary sensitive data in tool parameters. <br>
Risk: Marketplace service and tool availability changes over time, so assumptions about available tools may be stale. <br>
Mitigation: Search and inspect available services and tool schemas before execution, then report the specific tool used and result. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/preston-thiele/skills/danube) <br>
- [Danube homepage](https://danubeai.com) <br>
- [Danube dashboard](https://danubeai.com/dashboard) <br>
- [Danube documentation](https://docs.danubeai.com) <br>
- [Danube MCP server](https://mcp.danubeai.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a DANUBE_API_KEY; generated guidance may include MCP configuration and Danube tool execution steps.] <br>

## Skill Version(s): <br>
8.0.12 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
