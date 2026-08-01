## Description: <br>
Build and run grounded business agents on agent4.io over MCP: agents, knowledge bases, load-on-demand skills, stateful Storylines, and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business operators use this skill to configure and manage agent4.io tenants through a remote MCP/API workflow, including grounded agents, knowledge bases, load-on-demand skills, page playbooks, usage checks, and Storyline automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs an agent to operate an agent4.io tenant with an API key. <br>
Mitigation: Use only the intended AGENT4_API_KEY, confirm the tenant with tenant_info before changes, and avoid sharing the key in prompts, logs, or public artifacts. <br>
Risk: Agent configuration, knowledge-base content, queries, and customer data may be sent to agent4.io for storage or processing. <br>
Mitigation: Send only documents, configurations, and customer data that are approved for processing on agent4.io. <br>
Risk: The skill can guide persistent tenant changes such as public shares, scheduled follow-ups, custom domains, and Storyline publishing. <br>
Mitigation: Review these changes before approving them and verify the resulting console links or tenant state after execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>
- [Publisher profile](https://clawhub.ai/user/hellojixian) <br>
- [agent4.io cookbook](https://agent4.io/cookbook) <br>
- [agent4.io MCP endpoint](https://api.agent4.io/v1/mcp) <br>
- [agent4.io](https://agent4.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline command and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENT4_API_KEY and a remote MCP connection to agent4.io.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
