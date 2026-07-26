## Description: <br>
Book real-world local services through Lokuli MCP, including provider search, availability checks, booking creation, and checkout handoff across 75+ service categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to search for local service providers, compare provider details, check availability and pricing, and create bookings through Lokuli after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may share user contact details with Lokuli during booking flows. <br>
Mitigation: Collect only the required name, email, and phone information after the user has selected a provider and approved the booking details. <br>
Risk: The skill can route users to Stripe checkout or create a cart that may be mistaken for final payment approval. <br>
Mitigation: Confirm the provider, service, appointment time, price, cancellation terms, and shared contact details before creating a booking or presenting checkout. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/lokuli-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC request examples and user-facing booking summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce provider details, availability options, pricing estimates, booking status, Stripe checkout URLs, and AP2 cart details.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
