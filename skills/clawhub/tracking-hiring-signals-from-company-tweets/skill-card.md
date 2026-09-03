## Description:

Tracks hiring signals and growth indicators from company Twitter accounts using apidojo's Tweet Scraper on Apify and returns structured company, role, team, post date, and growth-signal information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, job seekers, talent intelligence teams, investors, and competitor analysts use this skill to monitor Twitter/X posts for early hiring and growth signals. It helps search, filter, score, deduplicate, and summarize hiring-related tweets into a hiring intelligence report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends tweet search queries to Apify and requires an Apify token.

Mitigation: Use an appropriate APIFY_TOKEN, confirm the queries are acceptable to send to Apify, and avoid embedding secrets in shared commands or outputs.

Risk: Large or broad searches can increase cost and produce excessive result volume.

Mitigation: Set maxItems plus start and end date filters before running the scraper.

Risk: Hiring signals from tweets may be stale, ambiguous, or dominated by job boards and aggregators.

Mitigation: Filter job-board and staffing terms, deduplicate by company handle, and verify tweet context and job links before making decisions.

Risk: Saved CSV or JSON exports can contain collected social-media data and inferred hiring intelligence.

Mitigation: Choose output filenames deliberately, store exports in the intended location, and review results before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-hiring-signals-from-company-tweets)
- [Apify Tweet Scraper run API](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with tables, inline shell commands, and optional CSV or JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include company handles, roles, teams, tweet dates, growth scores, role distribution, and saved CSV or JSON exports.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
