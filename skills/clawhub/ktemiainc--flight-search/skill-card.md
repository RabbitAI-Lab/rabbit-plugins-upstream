## Description:

Searches and compares one-way, round-trip, and multi-city flights using Ktemia, returning fares and seller booking links, and looks up airport or city codes when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel assistants use this skill to look up airport or airline codes and compare one-way, round-trip, or multi-city fares for specified dates. It returns itinerary details and seller booking links; the traveler completes booking on the seller's site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight searches use an external API and an environment API key; security scan coverage is partial.

Mitigation: Use the API only if you trust Ktemia, keep KTEMIA_API_KEY private, and review the partial scan coverage before relying on it for deployment decisions.

## Reference(s):

- [Ktemia Flight Search API](https://www.ktemia.com/docs/api/flights/search/)
- [Ktemia API Documentation](https://www.ktemia.com/docs/api/)
- [API Authentication](https://www.ktemia.com/docs/api/#authentication)
- [API Errors](https://www.ktemia.com/docs/api/#errors)
- [Ktemia API Key Account](https://app.ktemia.com)
- [ClawHub Skill Page](https://clawhub.ai/ktemiainc/skills/flight-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Booking links]

**Output Format:** [Structured flight search results presented as concise text with seller booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes itinerary times, stops, duration, seller, and per-person and total prices when available; does not book tickets.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata; artifact/SKILL.md declares 0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
