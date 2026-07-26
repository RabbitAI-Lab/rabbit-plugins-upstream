## Description: <br>
Book pet-grooming services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for pet-grooming providers, check availability, and create bookings through Lokuli's MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking sends customer name, email, and phone number to Lokuli. <br>
Mitigation: Confirm the provider, time slot, and contact details with the user before creating a booking. <br>
Risk: Search, availability, and booking results come from an external Lokuli MCP service. <br>
Mitigation: Review external service responses and verify booking details before treating a reservation as final. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-pet-grooming) <br>


## Skill Output: <br>
**Output Type(s):** [API calls, guidance, configuration] <br>
**Output Format:** [Markdown instructions with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lokuli MCP over SSE/JSON-RPC and may send customer contact details when creating a booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
