## Description:

Resolves arbitrary destinations with Gaode POI data, then queries Feizhu for nearby hotels, live prices, availability, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[han815757857-cmd](https://clawhub.ai/user/han815757857-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to find hotels near a specified destination for selected dates, with optional price, star-rating, and nearby-dining filters.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The POI lookup sends the API key and destination searches over an unencrypted connection.

Mitigation: Verify who operates the POI service, require an authenticated HTTPS integration, use only a key issued for that service, and rotate any key previously used over the HTTP connection.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/han815757857-cmd/skills/gaode-hotel)
- [Publisher profile](https://clawhub.ai/user/han815757857-cmd)
- [FlyAI service](https://open.fly.ai/)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown hotel listings with prices and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings may include hotel images, prices, ratings, nearby-destination details, and optional nearby dining results.]

## Skill Version(s):

1.0.0 (source: frontmatter metadata, CHANGELOG, released 2026-10-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
