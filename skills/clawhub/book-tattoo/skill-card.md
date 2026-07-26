## Description: <br>
Helps users search for tattoo services, check appointment availability, and create bookings through Lokuli's MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to find tattoo providers, check available appointment slots, and submit bookings through Lokuli after confirming contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking requests may send the user's name, email, and phone number to an external booking service. <br>
Mitigation: Before creating a booking, confirm the artist or provider, service, time slot, and contact details with the user. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill listing](https://clawhub.ai/edwardrodriguez703-design/skills/book-tattoo) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with JSON-RPC tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve external MCP requests that pass booking and customer contact details to Lokuli.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
