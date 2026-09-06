## Description:

Monitors Google News coverage for a brand using apidojo's Google Search scraper on Apify, returning article titles, publications, dates, URLs, and coverage sentiment per article.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

PR agencies, communications teams, brand managers, and reputation monitoring services use this skill to track brand, executive, and competitor coverage in Google News and identify coverage volume, sentiment, publications, and items needing PR attention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand, company, or investigation search terms are sent to Apify when the scraper is run.

Mitigation: Use this skill only when sharing those queries with Apify is acceptable, and avoid sensitive monitoring terms unless that disclosure has been approved.

Risk: Saved report filenames and outputs may expose monitored brands, topics, or article URLs on the local system.

Mitigation: Choose output filenames carefully and store generated CSV or JSON files only in locations appropriate for the sensitivity of the monitoring work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/monitoring-google-news-coverage-for-brand)
- [Apify Google Search Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~google-search-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, plus optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include headline classifications, sentiment labels, PR attention flags, and saved local report files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
