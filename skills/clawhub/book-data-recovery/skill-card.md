## Description: <br>
Book data-recovery services through Lokuli MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and assistants use this skill to search for data-recovery services, check availability, and create bookings through Lokuli. Booking workflows should confirm the provider, service, time slot, and customer contact details before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking may send the customer's name, email, and phone number to Lokuli. <br>
Mitigation: Confirm the provider, service, time slot, and contact details with the user before creating a booking. <br>
Risk: The skill depends on Lokuli as an external booking service. <br>
Mitigation: Install and use the skill only when the user is comfortable relying on Lokuli for data-recovery service discovery and booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, configuration] <br>
**Output Format:** [Markdown with JSON-RPC examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces booking workflow guidance and MCP tool-call argument examples for search, availability checks, and booking creation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
