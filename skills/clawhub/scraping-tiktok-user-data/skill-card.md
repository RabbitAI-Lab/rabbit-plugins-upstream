## Description:

Scrapes TikTok profile or video URLs with Apify's apidojo/tiktok-user-scraper actor to return creator video history and per-video engagement metrics for analysis and benchmarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect TikTok creator video history and engagement metrics for content analysis, auditing, and competitive benchmarking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect TikTok account, video, follower, or following data through Apify, which may create privacy or terms-of-service exposure.

Mitigation: Set collection limits, avoid follower and following extraction unless necessary, and verify compliance with TikTok terms and privacy obligations before use.

Risk: The workflow requires APIFY_TOKEN and includes REST examples that pass the token in URLs.

Mitigation: Treat APIFY_TOKEN as a secret, prefer safer authentication methods when available, and review scripts/run_actor.js before execution.

Risk: The actor uses pay-per-result billing, so broad collection can increase cost.

Mitigation: Set maxVideos or maxItems before running and confirm the expected collection scope with the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-user-data)
- [Apify actor: apidojo/tiktok-user-scraper](https://apify.com/apidojo/tiktok-user-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include per-video metrics such as video ID, caption, views, likes, comments, shares, duration, post timestamp, video URL, music title, and hashtags.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
