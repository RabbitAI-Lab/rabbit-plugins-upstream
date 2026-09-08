## Description:

Extracts tweets, reply threads, and engagement metrics from a specific Twitter/X profile using apidojo's Twitter Profile Scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, social media monitors, journalists, and competitive intelligence teams use this skill to collect public Twitter/X profile tweet data, reply threads, and engagement metrics for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target handles, profile URLs, date filters, and collection limits are sent to Apify.

Mitigation: Use only when the Apify account, retention practices, and target-list sensitivity are acceptable.

Risk: Public profile scraping can return no data for private accounts or errors for suspended accounts.

Mitigation: Handle empty or failed results explicitly and avoid presenting them as complete public activity records.

Risk: Very large profile collections can increase external service cost.

Mitigation: Set maxItems and date filters before running broad collections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-twitter-profile-tweets)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Twitter Profile Scraper run API](https://api.apify.com/v2/acts/apidojo~twitter-profile-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with command examples and JSON input/output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to request public Twitter/X profile tweet data and export results as table, CSV, or JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
