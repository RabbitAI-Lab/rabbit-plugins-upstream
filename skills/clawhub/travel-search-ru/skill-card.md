## Description:

Searches current Russian-catalog package tours, hotels, flights, excursions, activities, prices, availability, and booking links for travel-planning requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[missial](https://clawhub.ai/user/missial)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to find current tours, hotel-only stays, flights, activities, prices, availability, and booking links from a Russian-language travel catalog. It is a search layer for itinerary planning and does not make bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search criteria such as destinations, dates, traveler counts, ages, budgets, and preferences are sent to an external travel service.

Mitigation: Do not include names, passport details, payment data, credentials, or unnecessary sensitive information in search inputs.

Risk: Returned travel options, prices, and availability may be incomplete, cached, or stale.

Mitigation: Treat results as search output, disclose cached flight prices when relevant, and verify selected options with the provider before booking guidance.

Risk: Travel constraints such as geography, dates, traveler composition, and budget can materially affect suitability and price.

Mitigation: Clarify hard constraints before searching, ask for child ages when needed for family pricing, and only show above-budget or out-of-scope alternatives after explicit user consent.

## Reference(s):

- [README](README.md)
- [Travel Search CLI usage](references/usage.md)
- [ClawHub skill page](https://clawhub.ai/missial/skills/travel-search-ru)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [JSON CLI responses summarized by the agent as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include prices, availability, provider fields, and booking links; the skill does not book travel or persist local data.]

## Skill Version(s):

2.1.1 (source: evidence.json release, SKILL.md metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
