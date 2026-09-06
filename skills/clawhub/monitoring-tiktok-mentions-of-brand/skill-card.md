## Description:

Monitors TikTok for brand mentions and product discussions using apidojo's TikTok scraper on Apify, returning creator, engagement, sentiment, and caption signals for brand monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Brand managers, community teams, crisis communications teams, and product marketers use this skill to monitor TikTok mentions, hashtags, and product discussions. It helps identify viral praise, criticism, advocates, and crisis signals from public TikTok content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok search terms, hashtags, and URLs are sent to Apify/Apidojo for processing.

Mitigation: Do not include confidential campaign names, regulated data, secrets, or highly sensitive crisis terms unless third-party processing is approved.

Risk: Unlimited or broad collection can increase third-party processing cost and data volume.

Mitigation: Use bounded keywords, start URLs, locations, and maxItems values appropriate to the monitoring task.

Risk: Lexical sentiment and crisis thresholds can misclassify posts or overstate emerging issues.

Mitigation: Review high-impact posts and complaint clusters before escalating conclusions or taking external action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-tiktok-mentions-of-brand)
- [Apify Actor API endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, API calls, Configuration guidance, Files]

**Output Format:** [Markdown report with tables, inline shell or API examples, and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports creator handles, views, likes, comments, sentiment signals, content types, caption previews, trending posts, crisis alerts, and top advocates.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
