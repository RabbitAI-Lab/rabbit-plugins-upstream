## Description: <br>
Book catering services through Lokuli MCP. Use when user needs to find and book catering. Triggers on requests like "book a catering", "find catering near me", or any catering service request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search catering providers through Lokuli, check availability, and create catering bookings with approved customer details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal contact details to Lokuli and create real catering bookings. <br>
Mitigation: Require explicit user approval of the provider, date, time, price, cancellation terms, and contact details before creating a booking. <br>
Risk: The skill depends on an external Lokuli service for catering search, availability, and booking results. <br>
Mitigation: Review returned provider details with the user and use the service only when the user is comfortable relying on Lokuli for the booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-catering) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration] <br>
**Output Format:** [Markdown instructions with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides an agent to search catering services, check availability, and create bookings through Lokuli.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
