## Description:

Scrapes YouTube videos matching keyword queries with Apify's apidojo YouTube scraper and returns video metadata such as title, channel, engagement counts, duration, publish date, and URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, SEO analysts, and market intelligence teams use this skill to collect YouTube search-result datasets for topics, channels, playlists, Shorts, handles, or trending videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The REST fallback places APIFY_TOKEN in URL query strings, which can expose the token through shell history, logs, or process listings.

Mitigation: Prefer supported Apify tooling or header-based authentication, keep APIFY_TOKEN in a protected environment or secret store, avoid committing .env files, and rotate any token that has already been used in URL-based commands.

Risk: The skill can collect more than keyword search results, including channel, playlist, Shorts, handle, and trending-video data.

Mitigation: Review the requested input scope before running the scraper and limit collection to data needed for the user's stated task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-videos-by-keyword)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON or CSV dataset output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN and can return video IDs, titles, channel data, engagement counts, durations, publish dates, URLs, thumbnails, and descriptions.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
