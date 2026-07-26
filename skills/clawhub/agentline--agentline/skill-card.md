## Description: <br>
Make phone calls, view received SMS, provision numbers, manage agents, and track billing through the AgentLine telephony API using REST or MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentline](https://clawhub.ai/user/agentline) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to AgentLine telephony for outbound calls, inbound SMS and call review, phone number provisioning, agent management, and billing checks. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: Persistent event polling can automatically surface private SMS bodies and call transcript content. <br>
Mitigation: Configure polling to show event metadata by default and require explicit user approval before displaying message bodies or transcript text. <br>
Risk: The skill can use AgentLine account authority for calls, number provisioning charges, and access to inbound messages and transcripts. <br>
Mitigation: Install only for accounts where that authority is acceptable, confirm before dialing or provisioning numbers, and check balance or billing before paid actions. <br>


## Reference(s): <br>
- [AgentlineHQ ClawHub Skill Page](https://clawhub.ai/agentline/agentline) <br>
- [AgentLine Publisher Profile](https://clawhub.ai/user/agentline) <br>
- [AgentLine Website](https://agentline.cloud) <br>
- [AgentLine API Base URL](https://api.agentline.cloud) <br>
- [AgentLine MCP Server](https://api.agentline.cloud/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with curl, JSON, Python, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENTLINE_API_KEY and may guide paid telephony actions such as calls and number provisioning.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
