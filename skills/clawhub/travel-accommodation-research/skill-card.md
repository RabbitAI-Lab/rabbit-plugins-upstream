## Description:

Helps agents research public stays across Airbnb, Agoda, Hotels.com, Trip.com, and Vrbo, plus flights and activities on Agoda, using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel researchers use this skill to compare public listings, inspect property and host reviews, and gather itinerary evidence without making bookings or payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel searches, dates, party details, property IDs, and request bodies are sent to Crawlora with the user's API key.

Mitigation: Use the skill only when comfortable sharing those inputs with Crawlora; protect the API key.

Risk: Prices, availability, reviews, and cancellation terms can change or differ from final booking terms.

Mitigation: Record source, retrieval time, travel dates, occupants, and currency; verify important decisions on the original travel site.

Risk: The short description omits Vrbo despite the skill offering Vrbo research routes.

Mitigation: Include Vrbo in the scope when reviewing requested searches and consult the endpoint reference for supported routes.

## Reference(s):

- [Travel accommodation endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/travel-accommodation-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Source-aware research summaries and structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Price and availability snapshots retain source, dates, occupancy, and currency; no booking or payment actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
