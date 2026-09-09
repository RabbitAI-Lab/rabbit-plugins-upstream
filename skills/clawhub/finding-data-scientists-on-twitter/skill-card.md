## Description:

Finds data scientists and ML engineers to recruit using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams, hiring managers, AI research labs, and data-driven startups use this skill to discover, enrich, and score potential data science and machine learning candidates from Twitter/X profile and activity signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends Twitter/X search terms, handles, and collected profile data to Apify and apidojo services.

Mitigation: Confirm the data processing is appropriate for recruiting use, avoid sensitive or unnecessary personal data, and use only data the user is allowed to process.

Risk: Unbounded or overly broad searches can collect more profile data than needed.

Mitigation: Set reasonable maxItems limits and narrow search terms, locations, or specialties to the recruiting need.

Risk: Exported CSV or JSON files may contain personal profile data.

Mitigation: Choose output filenames and storage locations deliberately and handle exported results according to the user's retention and access policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-data-scientists-on-twitter)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Twitter user scraper actor](https://api.apify.com/v2/acts/apidojo~twitter-user-scraper/runs?token=$APIFY_TOKEN)
- [Apify tweet scraper actor](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown candidate report with tables, inline shell commands, and optional CSV or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Twitter/X handles, names, inferred ML specialty, stack signals, follower counts, activity status, open-to-work signals, candidate scores, and short bio highlights.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
