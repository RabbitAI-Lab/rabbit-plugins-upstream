## Description: <br>
Book plumber services through Lokuli MCP for finding plumbers, checking availability, and creating bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for plumber services through Lokuli, check provider availability, and create an appointment after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal contact and booking details to Lokuli. <br>
Mitigation: Require user consent before sending name, email, phone, provider, service, or time-slot details to the external MCP service. <br>
Risk: The skill can create a real plumber appointment. <br>
Mitigation: Require explicit final approval before calling create_booking, including provider, service, date, time, and contact details. <br>
Risk: External search may contact Lokuli with location or service intent. <br>
Mitigation: Ask before external search and limit query details to what is needed for provider discovery. <br>


## Reference(s): <br>
- [Book Plumber on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-plumber) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require user contact details and explicit approval before booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
