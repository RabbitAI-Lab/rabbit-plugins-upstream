## Description:

Pulls structured YouTube data -- video and channel details, transcripts/captions, comments, playlists, and search -- via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve public YouTube transcripts, comments, video and channel metadata, playlists, and search results through Crawlora for summarization, sentiment review, and content research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends requested YouTube targets and search queries to Crawlora.

Mitigation: Use only for public YouTube research, avoid sensitive query content, and provide the API key through CRAWLORA_API_KEY rather than hardcoding it.

Risk: The helper script is a generic authenticated API client and is broader than the YouTube-only purpose described by the skill.

Mitigation: Review requested paths before execution and prefer restricting use to the documented YouTube GET endpoints.

Risk: CRAWLORA_API_BASE can be overridden, which could send the API key to an unintended destination.

Mitigation: Check or unset CRAWLORA_API_BASE before running the helper, and pin requests to https://api.crawlora.net/api/v1 in controlled environments.

## Reference(s):

- [YouTube Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested public YouTube targets and queries to the Crawlora API.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
