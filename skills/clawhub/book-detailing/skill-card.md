## Description: <br>
Book Detailing helps agents search for detailing services, check availability, and create bookings through Lokuli's MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to find detailing providers, check available appointment times, and submit a booking through Lokuli. Before booking, users should confirm the provider, service, time slot, and contact details that will be sent to the booking provider. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking creation sends the user's name, email, phone number, selected provider, selected service, and time slot to Lokuli's external booking service. <br>
Mitigation: Confirm the provider, service, time slot, and contact details with the user before creating a booking. <br>
Risk: The skill depends on an external booking endpoint for provider search and availability. <br>
Mitigation: Treat returned providers and time slots as external service results and ask the user to confirm selections before booking. <br>


## Reference(s): <br>
- [Book Detailing on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-detailing) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Text with JSON-RPC MCP tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lokuli's external booking endpoint for search, availability checks, and booking creation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
