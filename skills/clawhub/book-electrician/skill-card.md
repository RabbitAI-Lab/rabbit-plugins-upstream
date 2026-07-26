## Description: <br>
Book electrician services through Lokuli MCP. Use when user needs to find and book electrician. Triggers on requests like "book a electrician", "find electrician near me", or any electrician service request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for electrician services, check provider availability, and create a booking through Lokuli's MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal contact details to an external booking service. <br>
Mitigation: Confirm the exact customer name, email, and phone number with the user before sending a booking request. <br>
Risk: The skill can create a real electrician booking without clear consent guardrails. <br>
Mitigation: Ask the user to confirm the provider, service, appointment time, and any available cost or cancellation terms before creating the booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-electrician) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider, service, availability, booking time, and customer contact details for Lokuli MCP tool calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
