## Description:

Searches Meituan chain-hotel package deals for Chinese cities, with filtering by city, brand, and discount or price sorting, and returns booking links for completing purchases on Meituan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-shopping agents use this skill to find discounted Meituan hotel packages, compare current deal prices, and open Meituan booking links. It is scoped to domestic Chinese cities and brand-hotel package search rather than general travel planning.

### Deployment Geography for Use:

China (domestic cities only)

## Known Risks and Mitigations:

Risk: Hotel search details are sent to a Tencent Cloud proxy.

Mitigation: Use the skill only when users accept that city, brand, and sort parameters are transmitted to that proxy.

Risk: Returned prices, inventory, and booking availability may change before purchase.

Mitigation: Have users confirm final price, availability, and terms on the Meituan booking page before ordering.

Risk: The skill is scoped to domestic Meituan hotel package search and may not satisfy broader travel-planning requests.

Mitigation: Route international, non-Meituan, or full-itinerary requests to a more appropriate travel-planning source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/meituan-hotel-deals)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted hotel deal list with images, prices, ratings, validity notes, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns up to 20 hotel package results per query; prices and inventory are real-time and must be confirmed on the Meituan booking page.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
