## Description: <br>
Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and assistants managing Calendly scheduling use this skill to list events, manage invitees, create scheduling links, check availability, cancel events, and administer organization invitations through Rube MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendly organization administration actions can change invitations or account membership. <br>
Mitigation: Review Calendly permissions before installation and require an explicit user approval step before inviting, revoking, or removing organization members. <br>
Risk: Event cancellation is irreversible and may notify invitees. <br>
Mitigation: Summarize the event details and affected invitees, then get explicit user confirmation before canceling an event. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/sohamganatra/skills/calendly-automation) <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with Calendly MCP tool sequences and parameter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active Calendly OAuth connection.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
