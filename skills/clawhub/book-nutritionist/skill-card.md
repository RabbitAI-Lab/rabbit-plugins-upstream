## Description: <br>
Book nutritionist services through Lokuli MCP when a user needs to find and schedule a nutritionist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to search for nutritionists, check availability, and create appointments through Lokuli. It is intended for booking workflows where the user confirms provider, time slot, and contact details before an appointment is created. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking sends customer name, email, and phone number to Lokuli as the external booking service. <br>
Mitigation: Before creating an appointment, review the provider and time slot and confirm the contact details the user wants to send. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-nutritionist) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [JSON-RPC MCP tool calls with concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search, availability, and booking calls may include zip code, provider and service identifiers, appointment time, and customer contact details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
