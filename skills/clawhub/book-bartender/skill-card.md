## Description: <br>
Book bartender services through Lokuli MCP for finding and booking bartender services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for bartender providers, check availability, and create bookings through Lokuli's MCP endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking requests send selected provider, service, date/time, and customer contact details to a third-party Lokuli endpoint. <br>
Mitigation: Before creating a booking, have the agent show the selected provider, service, date/time, and contact details for explicit user confirmation. <br>
Risk: Users may disclose personal information while booking an external service. <br>
Mitigation: Ask users to share only the personal information they are willing to send to Lokuli. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardrodriguez703-design/skills/book-bartender) <br>
- [Lokuli MCP Endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [Markdown with JSON-RPC tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a disclosed SSE MCP endpoint; booking calls may include customer contact details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
