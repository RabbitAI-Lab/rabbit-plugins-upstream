## Description: <br>
Book Salon helps agents find and book salon services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill through an agent to search for salons, check appointment availability, and create salon bookings with customer contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal contact details to an external Lokuli booking endpoint when creating an appointment. <br>
Mitigation: Before creating a booking, confirm the salon, service, time, customer name, email, and phone number with the user. <br>
Risk: A booking action may create a real appointment if the user or agent sends incorrect service, provider, or time-slot details. <br>
Mitigation: Use the search and availability steps first, then ask the user to approve the exact appointment details before calling create_booking. <br>


## Reference(s): <br>
- [Book Salon on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-salon) <br>
- [Lokuli MCP Endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON-RPC 2.0 MCP tool calls with concise agent-facing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include salon search criteria, availability dates, booking time slots, and customer name, email, and phone number.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
