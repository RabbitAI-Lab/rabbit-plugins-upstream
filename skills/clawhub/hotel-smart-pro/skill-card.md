## Description:

酒店智能搜索 provides five natural-language tools for domestic hotel search, Marriott brand search and details, package lookup, and nearby food recommendations using Fliggy and Gaode data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to search domestic China hotels, Marriott properties, hotel packages, and nearby restaurants, then review result links before completing bookings on external platforms.

### Deployment Geography for Use:

Global, with hotel and food search coverage documented for domestic China only.

## Known Risks and Mitigations:

Risk: Hotel, food, and location search text is sent to the skill publisher's cloud proxy and then to Fliggy or Gaode.

Mitigation: Avoid entering sensitive personal itinerary details unless the user accepts that data flow.

Risk: Hotel prices, availability, and package details can change after the skill returns results.

Mitigation: Verify current terms, pricing, and availability on the external booking page before making travel decisions.

Risk: The skill may include extra travel suggestions that are prompts rather than supported booking actions.

Mitigation: Treat suggestions as optional follow-up queries and confirm that the requested action is supported before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-smart-pro)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-like text with hotel, package, and food results, including prices, ratings, addresses, data-source notes, and external booking links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on external proxy, Fliggy, and Gaode responses; prices and availability can change, and booking is completed outside the skill.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
