## Description:

Outbound Travel Assistant helps users plan international travel with tools for flights, hotels, visa requirements, safety ratings, plug and voltage standards, tax refunds, currency conversion, baggage, seat maps, emergency contacts, and hotel details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to look up international travel logistics, estimate shopping tax refunds, compare flight and hotel options, and retrieve destination-specific safety and emergency information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight, hotel, seat, baggage, and hotel-detail queries are sent to the RG cloud proxy, and currency codes are sent to a public exchange-rate API.

Mitigation: Install only when that data sharing is acceptable, and keep RG_PROXY and PROXY_TOKEN configured by trusted operators.

Risk: Visa, safety, emergency, tax-refund, price, and booking information can be incomplete or time-sensitive.

Mitigation: Verify travel requirements, official safety guidance, emergency contacts, final prices, refund amounts, and booking terms against official or provider sources before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/outbound-travel-assistant)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON strings and concise natural-language travel guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include booking links, prices, currency rates, and country-specific travel data; verify time-sensitive details before acting.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
