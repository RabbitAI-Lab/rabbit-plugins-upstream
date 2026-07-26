## Description: <br>
Book real-world local services through Lokuli MCP, including search, availability checks, booking creation, payment links, carts, pricing estimates, and serviceability checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find local service providers, compare service details and pricing, check availability, and create a booking or cart only after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can share customer contact details with Lokuli and create payment links after confirmation. <br>
Mitigation: Before approving a booking or cart, verify the provider, service, time, price, cancellation terms, contact details being shared, and Stripe checkout destination. <br>
Risk: Local-service search or booking results may not match the user's intent or service area. <br>
Mitigation: Confirm the requested service, ZIP code, selected provider, and availability with the user before booking. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/lokuli-service-booking) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, text, configuration] <br>
**Output Format:** [Markdown guidance with JSON-RPC MCP tool-call examples and booking/payment links returned by the service] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return provider details, availability, pricing estimates, booking status, Stripe checkout URLs, or AP2 cart data depending on the selected MCP tool.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
