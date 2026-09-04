## Description:

Tracks brand sentiment across Twitter, Reddit, and TikTok using Apidojo's Apify scrapers, returning per-platform sentiment distribution, a cross-platform health score, influential posts, and theme analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, communications, PR, and reputation-management teams use this skill to monitor public discussion of a brand across social platforms and compare per-platform sentiment, themes, and impact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit collection may be unreliable because the evidence says the Reddit steps appear to call a Twitter scraper.

Mitigation: Review and correct the Reddit actor configuration before relying on Reddit sentiment or cross-platform health scores.

Risk: Search terms and collected social data may be sent to Apify-operated services.

Mitigation: Use the skill only for monitoring terms appropriate for Apify processing and store generated CSV or JSON outputs in a controlled location.

Risk: APIFY_TOKEN exposure could allow unauthorized actor usage.

Mitigation: Keep APIFY_TOKEN out of shared logs and shell history where possible and provide it through controlled environment configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-brand-sentiment-across-platforms)
- [ClawHub publisher profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown report with tables, sentiment scores, themes, post excerpts, and optional CSV or JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN and may call Apify actors for social-platform collection.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
