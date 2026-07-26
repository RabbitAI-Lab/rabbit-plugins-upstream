## Description: <br>
Book Tailor helps agents find tailor services, check availability, and create bookings through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can ask an agent to search for local tailor services, check appointment availability, and create a booking after confirming the provider, service, time, and contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking requests may send the user's name, email, phone number, selected provider, service, and appointment time to an external tailor-booking service. <br>
Mitigation: Before creating a booking, confirm the provider, service, appointment time, and exact contact details with the user. <br>
Risk: The skill depends on Lokuli's external MCP service, so search, availability, or booking results may be unavailable or change outside the agent's control. <br>
Mitigation: Tell the user when the service cannot complete a step and avoid presenting unconfirmed availability or bookings as final. <br>


## Reference(s): <br>
- [Book Tailor on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-tailor) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce search, availability, and booking requests for Lokuli MCP after user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
