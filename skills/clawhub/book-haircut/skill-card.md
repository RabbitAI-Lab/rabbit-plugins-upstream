## Description: <br>
Book haircut services through Lokuli MCP by helping users find appointment options and create bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to search for haircut services, check appointment availability, and create bookings through Lokuli. It is intended for haircut-related service requests where the user is comfortable sharing booking details with Lokuli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send personal booking details, including name, email, phone number, location, selected provider, service, and time, to Lokuli. <br>
Mitigation: Confirm the provider, time, service, and personal details with the user before creating a booking. <br>
Risk: The skill depends on Lokuli as an external booking provider for search results, availability, and appointment creation. <br>
Mitigation: Use the skill only when the user accepts Lokuli as the booking provider and verify returned appointment details before finalizing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-haircut) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC MCP tool call details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lokuli MCP search, availability, and booking actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
