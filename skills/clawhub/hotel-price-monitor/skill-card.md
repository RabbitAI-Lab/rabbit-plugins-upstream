## Description:

Hotel Price Monitor helps users search hotel options, compare real-time prices across travel platforms, and create structured price-watch requests for selected hotels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare hotel prices by city, hotel name, and stay dates, then decide whether to book, keep watching, or request a structured price monitor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel names, cities, dates, and related search parameters are sent through publisher proxy services.

Mitigation: Use only when sharing those travel query details with the publisher's proxy services is acceptable.

Risk: The release includes a reusable proxy token.

Mitigation: Treat token exposure as a publisher security issue and require publisher-side token rotation or scoped access before broad deployment.

Risk: Some same-price booking links may be ordered by commission preference.

Mitigation: Review all displayed platform options instead of assuming the first same-price link is the neutral best choice.

Risk: Monitoring behavior depends on the host agent carrying out future checks and notifications.

Mitigation: Confirm that the host agent supports scheduled rechecks and notification delivery before relying on price-watch requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-price-monitor)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, json, shell commands]

**Output Format:** [Markdown guidance with JSON hotel search, price comparison, and price-watch request outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include hotel names, prices, ratings, cancellation-policy summaries, booking links, and structured monitoring requests.]

## Skill Version(s):

1.1.7 (source: server release evidence; artifact frontmatter reports 1.1.1 and artifact/_meta.json reports 1.1.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
