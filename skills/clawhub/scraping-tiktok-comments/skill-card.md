## Description:

Scrapes comments from TikTok video URLs using apidojo's TikTok Comments scraper on Apify and returns commenter usernames, comment text, like counts, reply counts, and timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, sentiment analysts, brand monitors, and content researchers use this skill to collect TikTok video comment datasets for sentiment analysis, community research, product feedback extraction, and export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target TikTok URLs, run metadata, and scraped comment data are sent to Apify/Apidojo under the user's Apify account.

Mitigation: Install and run only when that data sharing is acceptable, and review Apify retention and deletion settings for actor runs and datasets.

Risk: Scraping regulated, sensitive, or high-volume monitoring targets can create privacy and compliance exposure.

Mitigation: Use reasonable maxItems limits and obtain approval before monitoring regulated or sensitive targets.

Risk: TikTok comments may be unavailable, disabled, deleted, filtered, or truncated.

Mitigation: Report unavailable or incomplete results clearly and avoid treating missing comments as a complete audience signal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-comments)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown table with inline shell commands and optional CSV or JSON export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs comment IDs, author usernames, comment text, like counts, reply counts, timestamps, reply markers, and parent comment IDs when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
