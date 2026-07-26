## Description: <br>
Book locksmith services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to find locksmith providers, check service availability, and create a locksmith booking through Lokuli MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal contact details to an external booking service. <br>
Mitigation: Confirm the user's intended name, phone, email, location, time, and final booking details before submitting a booking. <br>
Risk: The security verdict is suspicious because the skill lacks clear consent or confirmation guidance for sending booking details externally. <br>
Mitigation: Require explicit user approval before making any create_booking call or transmitting personal information. <br>


## Reference(s): <br>
- [Book Locksmith on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-locksmith) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Markdown and JSON-RPC call arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may collect customer name, email, phone number, location, requested service, and booking time for external booking requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
