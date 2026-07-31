## Description: <br>
Build and run grounded business agents on agent4.io over MCP, including agents, knowledge bases, load-on-demand skills, stateful Storylines, and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to agent4.io over MCP, configure grounded business agents, build knowledge bases, author load-on-demand skills, publish Storylines, and manage page playbooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected agent configuration, uploaded knowledge content, queries, and tenant or user metadata are sent to agent4.io under the tenant API key. <br>
Mitigation: Review the data passed into agent-building and knowledge-base tools, and send only content intended for the hosted service. <br>
Risk: The AGENT4_API_KEY grants access to the tenant's agent4.io service. <br>
Mitigation: Store the key as a secret or environment variable, and revoke or rotate it from the agent4.io console when it is no longer needed. <br>


## Reference(s): <br>
- [agent4.io Cookbook](https://agent4.io/cookbook) <br>
- [agent4.io](https://agent4.io) <br>
- [agent4.io REST API Reference](https://agent4.io/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>
- [Publisher Profile](https://clawhub.ai/user/hellojixian) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENT4_API_KEY and a remote MCP connection to agent4.io.] <br>

## Skill Version(s): <br>
1.0.34 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
