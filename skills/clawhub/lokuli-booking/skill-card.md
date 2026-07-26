## Description: <br>
Lokuli Booking helps agents search for, check availability for, and book local real-world services through the Lokuli MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People using an agent to find and book local services can compare providers, review availability and pricing, and create a booking only after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A booking workflow may create a real-world appointment or payment step before the user has reviewed the details. <br>
Mitigation: Verify the provider, service, time, price, cancellation terms, and contact details, then proceed only after explicit user approval. <br>
Risk: ZIP code and customer contact information may be shared with Lokuli, the selected provider, and Stripe-linked payment flows. <br>
Mitigation: Collect only the information needed for the requested booking and tell the user where it will be used before creating the booking or checkout link. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Guidance] <br>
**Output Format:** [Markdown or plain text summaries with MCP tool-call arguments and returned booking links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before booking and may return Stripe checkout URLs for payment.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
