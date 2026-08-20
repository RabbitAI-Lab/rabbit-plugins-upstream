## Description:

Traveler generates structured day-by-day travel itineraries from a user's origin, destination, trip length, budget, traveler profile, and interests, including timelines, local transport, meals, lodging notes, budget estimates, pitfalls, and backup plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onsoul](https://clawhub.ai/user/onsoul)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn travel ideas into actionable daily itineraries for solo, couple, family, parent-child, friends, or group trips. It plans routes, pacing, dining, lodging notes, budget ranges, and fallback options while directing booking, ticketing, ride-hailing, and restaurant actions to separate third-party skills or official apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad travel-adjacent requests and suggest installing Didi, Ctrip, or Meituan skills for rides, tickets, transit, or dining.

Mitigation: Confirm that the user wants travel planning and present third-party skill installation only as an optional execution path for itinerary actions that actually require it.

Risk: Itinerary details such as opening hours, ticket prices, reservations, transport durations, and crowding may be time-sensitive or location-dependent.

Mitigation: Label time-sensitive details as estimates and direct the user to verify them before travel or purchase.

Risk: Users may confuse planning guidance with completed bookings or orders.

Mitigation: Clearly state that the skill only plans and that bookings, ride-hailing, ticket purchases, restaurant reservations, and orders must be completed through separate third-party skills or official apps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/onsoul/skills/traveler)
- [ClawHub publisher profile](https://clawhub.ai/user/onsoul)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown itinerary with headings, tables, timelines, budget ranges, caveats, and execution suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions for missing preferences, time-sensitive verification caveats, and suggestions to install third-party Didi, Ctrip, or Meituan skills; it does not place bookings or orders.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
