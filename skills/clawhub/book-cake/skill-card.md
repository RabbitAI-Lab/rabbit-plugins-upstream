## Description: <br>
Book Cake helps agents search for cake services, check availability, and create bookings through Lokuli's MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find cake providers, check service availability, and create a booking after confirming provider, service, time, and customer contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking sends customer name, email, and phone number to Lokuli's external MCP service. <br>
Mitigation: Confirm the provider, service, time, and contact details with the user before creating a booking. <br>
Risk: The broad cake-service trigger scope may activate during general cake-service requests. <br>
Mitigation: Confirm that the user intends to search, check availability, or book before calling external tools. <br>


## Reference(s): <br>
- [Book Cake on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-cake) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SSE transport and JSON-RPC 2.0 over POST requests; booking examples include customer name, email, and phone number.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
