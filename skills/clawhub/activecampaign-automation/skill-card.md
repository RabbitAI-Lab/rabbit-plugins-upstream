## Description: <br>
Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Operators, marketers, and support teams use this skill to guide an agent through ActiveCampaign contact lookup, contact creation, tag management, list subscription changes, automation enrollment, and contact task creation through Rube MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to mutate ActiveCampaign records, including contacts, tags, list subscriptions, automation enrollment, and tasks. <br>
Mitigation: Confirm exact contacts, list IDs, tags, automation IDs, task details, and intended action before executing mutating tool calls. <br>
Risk: Subscription and bulk marketing changes can affect consent status or make broad account changes. <br>
Mitigation: Confirm marketing consent, subscription intent, and batch scope before subscribe, unsubscribe, or bulk tagging workflows. <br>
Risk: Incorrect schemas, action capitalization, ID formats, or stale tool assumptions can cause failed or unintended ActiveCampaign operations. <br>
Mitigation: Search current Rube tool schemas first, resolve IDs from ActiveCampaign, pass IDs as strings, and use backoff or spacing for bulk operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/activecampaign-automation) <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown instructions with MCP tool sequences and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active ActiveCampaign connection.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
