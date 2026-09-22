## Description:

Tuniu Travel Assistant helps agents search and book hotels, flights, trains, scenic tickets, cruises, and vacation products, with formatted results and related travel recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan travel, compare availability and prices, and initiate bookings for hotels, flights, trains, scenic tickets, cruises, and vacation packages through Tuniu-backed proxy tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or cancel travel orders and transmit traveler identity or contact data through a proxy.

Mitigation: Before any hotel, flight, train, or ticket order or cancellation, require explicit user approval and show the traveler, contact, and order data that will be sent.

Risk: The security verdict is suspicious because confirmation behavior and structured declarations are incomplete.

Mitigation: Review the skill before installation and use it only when Tuniu travel search and booking behavior is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tuniu-travel-assistant)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [JSON responses containing formatted Markdown travel results, errors, or booking/order data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prices, availability, itinerary details, images, booking identifiers, and related service recommendations returned by the travel platform.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
