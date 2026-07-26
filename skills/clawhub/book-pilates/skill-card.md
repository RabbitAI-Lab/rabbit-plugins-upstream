## Description: <br>
Book Pilates helps agents find Pilates services, check availability, and create bookings through the Lokuli MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for Pilates providers, check availability, and create bookings through Lokuli. Agents should present provider, service, time, price when available, and contact details for explicit user approval before sending personal information or creating a reservation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create real Pilates reservations through an external service using personal contact details. <br>
Mitigation: Require explicit user approval of the provider, service, time, price when available, and exact contact details before creating a booking. <br>
Risk: The skill contacts an external MCP service for search, availability, and booking actions. <br>
Mitigation: Use the skill only when the user intends to search for or book Pilates through Lokuli, and disclose external service use before sending booking details. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-pilates) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use an external MCP service to search providers, check availability, and create real bookings with user contact details.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
