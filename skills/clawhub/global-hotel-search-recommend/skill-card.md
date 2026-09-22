## Description:

Searches global hotel options and returns scene-aware recommendations with booking links, price tiers, and cancellation-policy summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel planners use this skill to turn a destination and optional natural-language travel request into hotel recommendations for business, family, vacation, backpacking, or general trips. The skill supports comparison and planning, while bookings are completed through returned booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel-search details such as destination, dates, travel query, party size, and child counts are sent to a cloud proxy.

Mitigation: Avoid entering unrelated sensitive personal information in the query and install only when this data flow is acceptable.

Risk: Returned prices, cancellation summaries, and filter matches may be inaccurate or relaxed when strict searches fail.

Mitigation: Treat results as planning guidance and verify price, availability, cancellation terms, and booking details on the destination booking page.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/global-hotel-search-recommend)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-formatted hotel recommendation text with prices, tags, reasons, cancellation summaries, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned prices and cancellation summaries are advisory and should be verified on the booking page.]

## Skill Version(s):

1.6.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
