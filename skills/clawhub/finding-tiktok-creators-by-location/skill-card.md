## Description:

Discovers TikTok creators and content by geographic location using apidojo's TikTok Location Scraper on Apify, returning creator profiles, verification status, hashtags, and engagement metrics for local influencer research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, agencies, and developers use this skill to collect and rank TikTok creators tied to a target place for local campaigns, geo-targeted influencer marketing, and regional market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using location-derived creator data can create privacy, platform-compliance, or misuse concerns.

Mitigation: Use only public, lawfully accessible data, respect TikTok terms and applicable privacy laws, and avoid harassment, stalking, or sensitive profiling.

Risk: The workflow depends on Apify access and an APIFY_TOKEN for actor execution.

Mitigation: Install only if Apify use is acceptable for the deployment environment and keep tokens scoped, private, and rotated according to local policy.

Risk: Geotagged posts may include tourists, stale posts, duplicate creators, or creators unrelated to the target local market.

Mitigation: Deduplicate by creator username, check profile or bio location signals, and sort by recency when freshness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-tiktok-creators-by-location)
- [Apify actor API endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-location-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API examples, ranking guidance, and optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TikTok location or place URLs as input and may output creator rankings based on followers, engagement, and verification status.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
