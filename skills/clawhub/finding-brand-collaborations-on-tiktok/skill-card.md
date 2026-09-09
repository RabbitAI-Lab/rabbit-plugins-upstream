## Description:

Discovers brand collaboration patterns and sponsored content on TikTok using apidojo's TikTok scrapers on Apify, returning creator handles, brand names, post performance, estimated reach, and collaboration frequency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, influencer marketing teams, competitive intelligence analysts, and brand partnership managers use this skill to find TikTok creator-brand partnerships, benchmark sponsored post performance, and map active campaigns in a product category.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Apify access and an APIFY_TOKEN for TikTok data collection.

Mitigation: Keep APIFY_TOKEN protected, avoid exposing it in logs or shared outputs, and configure output paths intentionally.

Risk: Scraped TikTok results may involve platform terms, privacy duties, and internal retention requirements.

Mitigation: Review platform terms, applicable privacy obligations, and data-retention rules before saving, sharing, or operationalizing results.

Risk: Sponsored content signals can be ambiguous or undisclosed, which may lead to incorrect brand-collaboration conclusions.

Mitigation: Treat inferred sponsorships as analyst findings, verify ambiguous brand mentions, and label uncertain creator-brand pairs before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-brand-collaborations-on-tiktok)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, optional shell commands, and optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include creator-brand pairs, campaign summaries, performance benchmarks, estimated reach, and collaboration frequency.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
