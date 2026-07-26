## Description: <br>
Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to automate Cal.com scheduling workflows through Rube MCP, including booking management, availability checks, webhook configuration, and team administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide account-changing Cal.com actions such as booking creation, team management, and webhook updates. <br>
Mitigation: Review each booking, team, webhook ID, trigger, and subscriber URL before approving any change. <br>
Risk: Webhook endpoints may receive personal and scheduling data, and webhook secrets function like credentials. <br>
Mitigation: Use trusted HTTPS webhook destinations under the user's control and protect webhook secrets as sensitive credentials. <br>


## Reference(s): <br>
- [Rube MCP](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, tool calls] <br>
**Output Format:** [Markdown with tool sequences and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an active Rube MCP connection and authenticated Cal.com connection before executing workflows.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
