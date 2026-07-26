## Description: <br>
Book Beauty helps agents search for beauty services through Lokuli, check availability, and create bookings after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to find beauty providers, compare services and pricing, check appointment availability, and create a booking only after explicit approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking may share customer contact details with Lokuli and the selected beauty-service provider. <br>
Mitigation: Before approving booking creation, verify the provider, service, appointment time, price, customer name, email, and phone number with the user. <br>
Risk: Search and availability results may not match the user's location, price expectations, or service preferences. <br>
Mitigation: Present provider options and pricing clearly, then ask the user to choose and confirm before checking availability or creating a booking. <br>


## Reference(s): <br>
- [Book Beauty on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/book-beauty) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC tool call examples and booking details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before creating a booking; booking may share contact details with Lokuli.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
