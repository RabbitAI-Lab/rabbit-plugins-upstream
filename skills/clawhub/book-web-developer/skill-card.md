## Description: <br>
Book web-developer services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to search for web-developer services, check provider availability, and create a booking through Lokuli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends customer name, email, and phone number to an external booking service. <br>
Mitigation: Confirm the user's intent to book and the exact contact details before creating a booking. <br>
Risk: A booking action can create an external service appointment. <br>
Mitigation: Confirm the selected provider, service, date, and time slot before calling create_booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-web-developer) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [Text and JSON-RPC tool-call arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include search criteria, provider and service identifiers, availability dates, time slots, and customer contact details needed for booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
