## Description:

Tracks and compares competitor follower growth and engagement benchmarks across Twitter/X, TikTok, and Instagram using apidojo Apify scrapers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing analysts, competitive intelligence teams, and growth leaders use this skill to compare public social audience size and engagement across competitor accounts. It supports recurring tracking so teams can observe growth velocity over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends public account handles and collected social metrics to Apify.

Mitigation: Install and run the skill only where sending those handles and metrics to Apify is acceptable.

Risk: The skill requires an APIFY_TOKEN credential for scraper execution.

Mitigation: Store APIFY_TOKEN as a protected environment secret and avoid exposing token-bearing URLs in shared logs or screenshots.

Risk: Recurring tracking can continue collecting data on a schedule after initial setup.

Mitigation: Review scheduled weekly automation before enabling it and periodically confirm that monitored handles remain appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-competitor-social-media-growth)
- [Apify Twitter user scraper](https://apify.com/apidojo/twitter-user-scraper)
- [Apify TikTok profile scraper](https://apify.com/apidojo/tiktok-profile-scraper)
- [Apify Instagram scraper](https://apify.com/apidojo/instagram-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with comparison tables and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public account handles, follower counts, engagement benchmarks, cross-platform summaries, and recurring tracking guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
