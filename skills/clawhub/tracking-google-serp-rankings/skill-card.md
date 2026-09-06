## Description:

Tracks Google search rankings and SERP features for any keyword using apidojo's Google Search scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External SEO managers, content strategists, and digital marketing agencies use this skill to check Google ranking positions, compare competitor visibility, and identify SERP features for selected keywords.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends keyword and search configuration data to Apify/apidojo through an external scraping actor.

Mitigation: Use only where Apify/apidojo processing is acceptable, and avoid submitting sensitive client or unreleased strategy terms unless permitted.

Risk: APIFY_TOKEN is required for actor execution.

Mitigation: Store APIFY_TOKEN in environment variables or approved secret storage, and avoid placing tokens in prompts, command history, or saved artifacts.

Risk: The customMapFunction parameter can execute transformation code supplied to the actor.

Mitigation: Do not use customMapFunction code from untrusted sources; review any function before execution.

Risk: Google rankings can vary by time, location, personalization, and SERP layout.

Mitigation: Treat results as time-bound snapshots and use consistent country, language, device, and run timing for comparisons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-google-serp-rankings)
- [API Dojo ClawHub publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor: apidojo/google-search-scraper](https://apify.com/apidojo/google-search-scraper)
- [Apify actor run API endpoint from artifact](https://api.apify.com/v2/acts/apidojo~google-search-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, API Calls, Code, Files]

**Output Format:** [Markdown report with ranking tables, optional shell commands, and optional JSON or CSV output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranking positions, URLs, titles, snippets, SERP feature labels, competitor summaries, and saved JSON or CSV exports.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
