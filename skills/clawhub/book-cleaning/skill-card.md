## Description: <br>
Book cleaning services through Lokuli MCP for users who need to find and book cleaning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for cleaning services through Lokuli, check availability, and create bookings with their contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send booking details, including customer contact information, to a third-party booking service. <br>
Mitigation: Before creating a booking, confirm the provider, service, time, price or terms when available, and the exact contact details that will be sent. <br>
Risk: Search and availability results depend on Lokuli's external MCP service. <br>
Mitigation: Treat provider availability and terms as service-provided data and ask the user to verify important booking details before submission. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-cleaning) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [JSON-RPC MCP tool calls and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use customer name, email, phone, ZIP code, provider, service, date, and time slot when creating bookings.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
