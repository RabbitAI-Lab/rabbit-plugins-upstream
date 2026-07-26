## Description: <br>
Book real-world local services through Lokuli MCP by finding providers, checking availability, and creating bookings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search for local service providers, compare pricing and availability, and create bookings only after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches and bookings may share contact details and service request information with Lokuli and payment providers such as Stripe. <br>
Mitigation: Review the provider, price, time, and contact details before approving a booking or opening a checkout link. <br>
Risk: Booking actions can affect real-world appointments or payments. <br>
Mitigation: Require explicit user confirmation before creating a booking, and show pricing upfront before checkout. <br>
Risk: Provider availability, serviceability, and pricing can vary by location and time. <br>
Mitigation: Validate the location, check availability, and use pricing estimates before presenting booking options. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [Local Booking on ClawHub](https://clawhub.ai/edwardrodriguez703-design/skills/local-booking) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Markdown or plain text summaries with JSON-RPC MCP tool calls and checkout URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider details, availability slots, pricing estimates, booking status, and Stripe checkout URLs after user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
