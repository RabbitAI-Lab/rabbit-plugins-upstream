## Description:

Global Flight Search helps agents search international flights and hotels, check seats and baggage, and provide outbound travel guidance for visas, safety, plug standards, tax refunds, exchange rates, and emergency help.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare itinerary options and retrieve supporting travel details before booking or departure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel, visa, safety, tax refund, and exchange-rate information may be stale or incomplete.

Mitigation: Verify visa, safety, embassy, tax, and exchange details against official sources before acting.

Risk: Flight, hotel, route, date, and itinerary details are sent to a configured RG cloud proxy, and currency codes are sent to a public exchange-rate API.

Mitigation: Install only where those data flows are acceptable; avoid entering sensitive personal data beyond itinerary parameters needed for lookup.

Risk: Booking links and prices are informational and may change.

Mitigation: Complete payments only on trusted booking sites after reviewing provider terms and current prices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/global-flight-search)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON-formatted text returned by tool calls, with concise travel details, disclaimers, and follow-up tips.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include booking URLs, prices, local emergency contacts, and travel disclaimers; does not complete purchases, bookings, or payments.]

## Skill Version(s):

1.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
