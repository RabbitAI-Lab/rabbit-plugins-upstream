## Description: <br>
Build and run grounded business agents on agent4.io over MCP: agents, knowledge bases, load-on-demand skills, stateful Storylines, and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure and operate agent4.io agents through a remote MCP server, including grounded agents, knowledge bases, load-on-demand skills, Storylines, page playbooks, usage checks, and shares. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-selected agent configuration, knowledge-base content, and queries may be sent to agent4.io. <br>
Mitigation: Use the skill only when this data transfer is intended, and avoid sending secrets or regulated/customer data unless approved. <br>
Risk: A user-provided agent4.io API key controls tenant access. <br>
Mitigation: Store the key in AGENT4_API_KEY, confirm the target tenant with tenant_info(), and rotate or revoke the key if it may have been exposed. <br>
Risk: Public shares and the broad REST API fallback can expose or change more than a narrow MCP recipe. <br>
Mitigation: Review share settings before publishing and review direct REST calls carefully before execution. <br>


## Reference(s): <br>
- [agent4.io Cookbook](https://agent4.io/cookbook) <br>
- [agent4.io](https://agent4.io) <br>
- [agent4.io MCP endpoint](https://api.agent4.io/v1/mcp) <br>
- [agent4.io REST API reference](https://agent4.io/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>
- [Publisher profile](https://clawhub.ai/user/hellojixian) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, MCP tool calls, JSON/REST examples, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENT4_API_KEY and remote agent4.io MCP access; may produce agent, knowledge base, skill, share, Storyline, and page playbook configurations.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
