## Description:

Monitors Twitter/X for competitor hiring announcements using apidojo's Tweet scraper and returns hiring signals such as role, department, posting date, urgency, growth pattern, and score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Competitive intelligence teams, recruiters, and investors use this skill to monitor Twitter/X job-posting signals, classify growth patterns, and summarize competitor hiring activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: APIFY_TOKEN can be exposed if placed directly in URLs, logs, or shell history.

Mitigation: Keep the token in the environment or a secret-aware client/helper, and avoid raw curl URLs that include token query parameters when possible.

Risk: Unbounded searches can create unpredictable Apify usage and overly broad data collection.

Mitigation: Set maxItems and narrow search terms or filters before running the scraper.

Risk: Saved competitive intelligence results may contain sensitive business information.

Mitigation: Choose an intended output location and access controls before saving CSV or JSON results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-twitter-for-competitor-job-posts)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Files, Analysis]

**Output Format:** [Markdown report with a results table and summary; optional CSV or JSON saved results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include growth classifications and relevance scores for returned hiring signals.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
