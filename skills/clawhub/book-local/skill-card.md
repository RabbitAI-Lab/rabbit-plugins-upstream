## Description: <br>
Book real-world local services through Lokuli MCP by helping an agent search providers, check availability, collect required contact details, and create confirmed bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to find local-service providers, compare pricing and availability, and generate a Stripe checkout link only after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may prepare a real booking or cart involving payment. <br>
Mitigation: Require explicit user confirmation of provider, service, price, time, and payment terms before creating a booking or cart. <br>
Risk: Booking requires sharing contact details with Lokuli and Stripe. <br>
Mitigation: Confirm the user's name, email, and phone number before sending them to the booking or checkout flow. <br>
Risk: Broad local-service triggers could activate the skill for casual service-search requests. <br>
Mitigation: Use the skill only when the user wants help with Lokuli local-service searches or bookings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-local) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [Markdown text with JSON-RPC MCP tool call arguments and booking or payment links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before booking and collection of name, email, and phone for checkout.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
