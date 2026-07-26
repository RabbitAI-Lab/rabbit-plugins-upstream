## Description: <br>
Book venue services through Lokuli MCP for users who need to search venues, check availability, and create bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find venues, check available time slots, and create a venue booking through Lokuli. Users should confirm venue details and personal contact information before a booking is created. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create bookings with personal contact details through an external service. <br>
Mitigation: Confirm the venue, time, price, cancellation terms, and exact personal contact details before creating a booking. <br>
Risk: The trigger scope is broad enough to activate for general venue-service requests. <br>
Mitigation: Use the skill only when the user clearly intends to search for or book a venue through Lokuli. <br>


## Reference(s): <br>
- [Book Venue on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-venue) <br>
- [Lokuli MCP Endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, text] <br>
**Output Format:** [Markdown with JSON-RPC request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a Lokuli MCP server over SSE and JSON-RPC 2.0.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
