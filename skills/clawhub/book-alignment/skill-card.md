## Description: <br>
Book alignment services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for alignment providers, check appointment availability, and create bookings through Lokuli's MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking requests send normal appointment contact details to Lokuli's external service. <br>
Mitigation: Confirm the exact name, email, phone number, provider, service, and appointment time before allowing a booking. <br>
Risk: The create_booking tool can submit an actual alignment appointment request. <br>
Mitigation: Require explicit user confirmation of the provider, service, and time slot before calling create_booking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-alignment) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Configuration] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SSE transport with JSON-RPC 2.0 calls to search, check availability, and create bookings.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
