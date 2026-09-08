## Description:

Scrapes TikTok videos for hashtags or keywords through apidojo's TikTok scraper on Apify and returns video metadata, engagement metrics, author details, captions, and timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, trend researchers, and social media teams use this skill to collect TikTok post metadata by hashtag, keyword, profile, music page, location, or search URL for analysis or export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok URLs, hashtags, keywords, and collected results are sent to Apify/apidojo.

Mitigation: Use only non-sensitive, authorized targets and avoid private, regulated, confidential, or sensitive investigations.

Risk: The REST fallback places APIFY_TOKEN in request URLs, which can be exposed through shell history, logs, or copied output.

Mitigation: Treat APIFY_TOKEN as a secret, prefer environment-based tooling, and avoid sharing command output or logs that include tokenized URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-videos-by-hashtag)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Configuration]

**Output Format:** [Markdown guidance with command examples and tabular TikTok metadata; optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN; results may include video URLs, captions, engagement counts, author handles, timestamps, music titles, hashtags, and ad indicators.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
