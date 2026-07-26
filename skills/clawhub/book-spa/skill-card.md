## Description: <br>
Book Spa helps an agent search Lokuli for spa services, check availability, and create bookings through Lokuli's MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find spa providers, check time slots, and prepare bookings through Lokuli after confirming appointment and contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A booking can send customer contact details and appointment details to Lokuli before the user has confirmed them. <br>
Mitigation: Confirm the provider, service, time slot, customer name, email, and phone number before creating a booking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-spa) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Text and JSON-RPC MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use spa search criteria, appointment details, and customer contact details when creating a booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
