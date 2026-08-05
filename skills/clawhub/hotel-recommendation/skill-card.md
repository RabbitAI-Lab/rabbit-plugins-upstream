## Description:

Uses the RollingGo CLI to search hotels, filter results, read hotel tags, and retrieve room pricing and hotel details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longcreat](https://clawhub.ai/user/longcreat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to find candidate hotels by destination, dates, budget, star rating, tags, brand, or distance, then inspect room availability and pricing before selecting a booking link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the RollingGo CLI to obtain live hotel results.

Mitigation: Confirm the RollingGo CLI package source is trusted before installation or execution.

Risk: The RollingGo API key may be exposed if passed directly on the command line or stored broadly.

Mitigation: Store the API key in scoped environment or secret configuration and avoid passing it as a command-line argument when possible.

Risk: Hotel search parameters are sent to RollingGo to obtain live results.

Mitigation: Share only the travel details needed for the query and avoid entering unnecessary sensitive information.

Risk: Live hotel availability, prices, refund policies, and booking links can change.

Mitigation: Verify the final price, policy, and availability on the booking page before purchase.

## Reference(s):

- [RollingGo homepage](https://rollinggo.store)
- [RollingGo API key application](https://rollinggo.store/apply)
- [RollingGo NPX reference](references/rollinggo-npx.md)
- [RollingGo UV reference](references/rollinggo-uv.md)
- [Claw host environment reference](references/claw-host-env.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RollingGo CLI commands, hotel IDs, room-price summaries, booking or hotel-detail URLs, and recommendations based on returned results.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
