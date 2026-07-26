## Description: <br>
Book Moving helps an agent search for moving services, check availability, and create bookings through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can ask an agent to find moving providers, check available dates or time slots, and prepare a booking through Lokuli. The user should confirm provider, timing, pricing, cancellation terms, and contact details before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking actions may send personal contact and move details to Lokuli or connected providers. <br>
Mitigation: Confirm provider, date, time, price, cancellation terms, name, email, phone number, and booking details with the user before submitting a booking. <br>
Risk: Search and availability results may change before the user commits to a booking. <br>
Mitigation: Check availability immediately before booking and ask the user to review the selected provider, service, date, and time slot. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [Natural-language responses plus JSON-RPC 2.0 MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May collect customer name, email, phone number, ZIP code, provider, service, date, and time slot for booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
