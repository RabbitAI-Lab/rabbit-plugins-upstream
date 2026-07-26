## Description: <br>
Book Piano Lessons helps an agent search for and book piano lessons through Lokuli's MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can ask an agent to find piano lesson providers, check availability, and prepare a booking through Lokuli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create a real booking through Lokuli using user contact details. <br>
Mitigation: Before calling create_booking, confirm the provider, service, date, time, customer name, email, and phone number with the user. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-piano-lessons) <br>
- [Publisher profile](https://clawhub.ai/user/edwardrodriguez703-design) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls] <br>
**Output Format:** [Text instructions with JSON-RPC tool call payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider, service, appointment time, and customer contact fields for Lokuli after user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
