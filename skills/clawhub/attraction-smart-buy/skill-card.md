## Description:

美团+途牛双平台景点门票实时比价，展示价差、可省金额和预订链接，帮你买到最低价门票。支持全国景点搜索含实景图片，含多票型引导提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travel users and agents use this skill to search attractions by city or keyword, compare Meituan and Tuniu ticket prices, and receive buying guidance with booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket searches and attraction names are sent through publisher-operated proxy services.

Mitigation: Install only if that data flow is acceptable, and require clear documentation of the exact external services involved.

Risk: A reusable proxy token is embedded in the artifact while PROXY_TOKEN is declared as the primary environment variable.

Mitigation: Rotate the exposed token and load credentials from the declared environment variable before broad use.

Risk: The skill returns monetized booking or referral links as part of ticket recommendations.

Mitigation: Disclose referral-link behavior to users and verify price, ticket type, and platform availability before purchase.

Risk: The public description includes 3-platform and broad ticket-type claims that the security guidance says need correction.

Mitigation: Correct the platform-count and ticket-type claims so users understand the actual data sources and coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/attraction-smart-buy)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [JSON from CLI tools and Markdown-style agent summaries with prices, savings, images, booking links, and ticket advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real-time third-party ticket data, referral booking links, and advisory signals based on platform prices and availability.]

## Skill Version(s):

3.3.1 (source: ClawHub release evidence; artifact frontmatter 2.0.4 and artifact _meta.json 3.3.0 differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
