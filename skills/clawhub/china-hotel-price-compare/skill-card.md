## Description:

Browses China hotel options and compares selected hotel prices across TourMind, Tuniu, Tongcheng, Meituan, and RollingGo with ratings, distance, breakfast, cancellation details, and booking links when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to browse China hotel options by city, date, area, landmark, budget, or rating, then compare a selected hotel across multiple travel platforms before booking externally.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Travel search details are sent to external hotel and proxy services.

Mitigation: Install only when the publisher and external data flow are acceptable for the intended users and avoid entering unnecessary personal details.

Risk: The artifact embeds shared proxy credentials in source.

Mitigation: Rotate or replace shared credentials before trusted deployment and limit access to the proxy endpoints.

Risk: Booking links are supplied by remote responses and may lead users away from the agent environment.

Mitigation: Verify destination URLs, hotel identity, dates, and final prices on the booking site before clicking, paying, or sharing payment information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-hotel-price-compare)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown hotel browsing and price-comparison summaries with inline booking links when returned by external services]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes hotel names, prices, ratings, location details, cancellation or breakfast notes, platform availability, price-difference warnings, and reminders that prices can change.]

## Skill Version(s):

4.1.6 (source: server release evidence; artifact frontmatter lists 4.1.1 and artifact metadata lists 4.1.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
