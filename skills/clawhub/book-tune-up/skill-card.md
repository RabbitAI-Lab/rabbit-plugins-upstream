## Description: <br>
Book tune-up services through Lokuli MCP. Use when user needs to find and book tune-up. Triggers on requests like "book a tune-up", "find tune-up near me", or any tune-up service request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for tune-up providers through Lokuli, check appointment availability, and create a booking after confirming appointment and contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking sends personal contact details and appointment information to Lokuli. <br>
Mitigation: Before calling create_booking, confirm the provider, service, date, time, customer name, email, phone number, ZIP code, and the user's consent to share those details. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub listing](https://clawhub.ai/edwardrodriguez703-design/skills/book-tune-up) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Configuration] <br>
**Output Format:** [Markdown guidance with JSON-RPC tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lokuli MCP over SSE and JSON-RPC 2.0; booking calls may include name, email, phone number, ZIP code, and appointment details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
