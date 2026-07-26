## Description: <br>
Book auto-body services through Lokuli MCP for users who need to find providers, check availability, and create auto-body service bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for auto-body providers, check appointment availability, and request bookings through Lokuli. It is intended for auto-body service requests that require provider, appointment, and customer contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking workflows may share sensitive customer contact details with Lokuli and selected service providers. <br>
Mitigation: Before final booking, show the provider, service, appointment time, customer name, email, and phone number, then require explicit user approval. <br>
Risk: A booking could be created with the wrong provider, service, appointment time, or contact information. <br>
Mitigation: Confirm all booking details with the user immediately before calling the booking tool. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardrodriguez703-design/skills/book-auto-body) <br>
- [Lokuli MCP Endpoint](https://lokuli.com/mcp/sse) <br>
- [Publisher Profile](https://clawhub.ai/user/edwardrodriguez703-design) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, configuration] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider search criteria, availability checks, booking details, and customer contact fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
