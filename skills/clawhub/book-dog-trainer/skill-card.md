## Description: <br>
Book dog-trainer services through Lokuli MCP for users who need to find and book dog-trainer appointments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for dog-trainer providers through Lokuli, check appointment availability, and create a booking after the user selects a service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send customer contact details to an external service. <br>
Mitigation: Show the exact name, email, and phone number that will be sent, and ask for explicit user approval before creating a booking. <br>
Risk: The skill can create a real dog-trainer booking without built-in confirmation instructions. <br>
Mitigation: Present the selected provider, service, appointment time, and price or terms when available, then require explicit approval before calling create_booking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-dog-trainer) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Markdown instructions with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send customer contact details to Lokuli MCP when creating a booking.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
