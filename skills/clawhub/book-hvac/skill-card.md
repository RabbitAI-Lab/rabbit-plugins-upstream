## Description: <br>
Book hvac services through Lokuli MCP. Use when user needs to find and book hvac. Triggers on requests like "book a hvac", "find hvac near me", or any hvac service request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and service-booking agents use this skill to search for HVAC providers through Lokuli, check appointment availability, and create HVAC service bookings with customer contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit real HVAC booking requests that include customer contact details. <br>
Mitigation: Confirm the provider, service, appointment time, customer name, email, and phone number with the user before invoking create_booking. <br>
Risk: The skill shares booking and contact information with Lokuli's service endpoint. <br>
Mitigation: Use the skill only when the user intends to search for or schedule HVAC service through Lokuli. <br>


## Reference(s): <br>
- [Book HVAC ClawHub listing](https://clawhub.ai/edwardrodriguez703-design/skills/book-hvac) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON-RPC MCP tool calls with concise booking confirmation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires provider, service, appointment time, and customer contact details before creating a booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
