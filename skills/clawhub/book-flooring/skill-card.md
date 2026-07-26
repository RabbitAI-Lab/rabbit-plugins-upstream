## Description: <br>
Book flooring services through Lokuli MCP for users who need to find flooring providers, check availability, and request a booking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to search for flooring services, check provider availability, and prepare a booking through Lokuli. Agents should present booking details for explicit user approval before creating a real booking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create a real flooring booking and send customer name, email, and phone number to Lokuli. <br>
Mitigation: Before calling create_booking, require the agent to show the provider, service, date, time, customer name, email, and phone number, then proceed only after explicit approval. <br>
Risk: The security verdict is suspicious because confirmation guidance is not clear in the artifact. <br>
Mitigation: Install only when the operator is comfortable using Lokuli for external flooring-service lookup and booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [Book Flooring on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-flooring) <br>
- [Publisher profile on ClawHub](https://clawhub.ai/user/edwardrodriguez703-design) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Markdown with JSON tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create real flooring bookings and transmit customer contact details through Lokuli when the agent calls the booking tool.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
