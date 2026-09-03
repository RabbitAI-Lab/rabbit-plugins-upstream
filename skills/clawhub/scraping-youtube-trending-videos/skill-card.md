## Description:

Extracts YouTube trending video data by category and country using apidojo's YouTube Trending Scraper on Apify, returning titles, URLs, engagement counts, channel details, descriptions, and thumbnails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, trend analysts, and YouTube marketers use this skill to collect YouTube trending video datasets by category, country, and language for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the Apify actor requires an APIFY_TOKEN and sends configured request data to Apify.

Mitigation: Store the token in an environment variable or secret manager, avoid exposing it in prompts or logs, and do not place secrets or private data in optional inputs such as custom transformation code.

Risk: Trending results are point-in-time snapshots and can vary by country, language, category, and session.

Mitigation: Record the type, country, language, and run time with downstream analysis, and retry or fall back to type=n when a category has no results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-trending-videos)
- [Apify actor REST API endpoint](https://api.apify.com/v2/acts/apidojo~youtube-trending-scraper/runs)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Files, Markdown]

**Output Format:** [Markdown table, JSON, or CSV depending on the requested output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns point-in-time YouTube trending video records with video, channel, engagement, keyword, live-status, and thumbnail fields.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
