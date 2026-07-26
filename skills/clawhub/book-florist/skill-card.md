## Description: <br>
Book Florist helps users search for and book florist services through Lokuli's external MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find florists, check service availability, and create florist bookings through Lokuli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Florist searches and bookings are sent to Lokuli's external MCP service. <br>
Mitigation: Review the service relationship before installation and confirm the provider, service, date, time, price or terms before creating a booking. <br>
Risk: Creating a booking can share customer name, email, and phone details with the external service. <br>
Mitigation: Proceed with create_booking only after the user confirms the contact details that will be shared. <br>


## Reference(s): <br>
- [Book Florist ClawHub page](https://clawhub.ai/edwardrodriguez703-design/skills/book-florist) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers search, availability checks, and booking creation through an external MCP service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
