## Description: <br>
Book real-world services through Lokuli MCP by helping users find providers, check availability, and create local service bookings across 75+ categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill through an agent to search for local service providers, compare pricing and availability, and create a confirmed booking that returns a Stripe checkout link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking details and customer contact information may be sent to an external service and provider. <br>
Mitigation: Only share contact details the user is willing to send to the booking service and provider. <br>
Risk: The skill can create real-world bookings and return Stripe checkout links for payment. <br>
Mitigation: Before approving a booking or opening the checkout link, verify the provider, service, price, date, and time with the user. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC tool call examples and returned booking or payment details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider details, pricing estimates, available time slots, booking status, and Stripe checkout URLs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
