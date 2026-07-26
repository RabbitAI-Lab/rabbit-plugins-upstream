## Description: <br>
Book barber services through Lokuli MCP for users who need to find and book barber appointments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to search Lokuli for barber providers, check appointment availability, and create a booking after confirming provider, service, time, and contact details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking requests may send user contact details to Lokuli. <br>
Mitigation: Before creating a booking, confirm the provider, service, time, customer name, email, phone number, and that the user wants those details sent. <br>
Risk: The skill can create booking requests through a third-party service. <br>
Mitigation: Require explicit user confirmation before calling the booking tool. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [MCP JSON-RPC tool calls with concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include booking details and user-provided contact details sent to Lokuli.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
