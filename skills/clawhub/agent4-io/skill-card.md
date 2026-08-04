## Description: <br>
Build and run grounded business agents on agent4.io over MCP — agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to agent4.io and build or manage grounded business agents, knowledge bases, load-on-demand skills, Storylines, page playbooks, usage checks, and user/session lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Knowledge-base material, agent configuration, and related queries are sent to agent4.io and handled by that platform. <br>
Mitigation: Confirm the intended data sharing before use and send only material appropriate for the agent4.io tenant. <br>
Risk: Tenant administration actions can affect a live agent4.io workspace. <br>
Mitigation: Use a dedicated tenant API key, confirm the target tenant, and review administrative changes before asking the agent to make them. <br>
Risk: Public share links or REST API actions can expose or change live resources. <br>
Mitigation: Review public links and REST API actions carefully before sharing or executing them. <br>


## Reference(s): <br>
- [agent4.io Cookbook](https://agent4.io/cookbook) <br>
- [agent4.io](https://agent4.io) <br>
- [agent4.io MCP endpoint](https://api.agent4.io/v1/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>
- [Publisher profile](https://clawhub.ai/user/hellojixian) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and MCP/API call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENT4_API_KEY and user-directed calls to agent4.io.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
