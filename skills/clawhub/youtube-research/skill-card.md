## Description:

Pulls structured YouTube data — video and channel details, transcripts/captions, comments, playlists, and search — via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to retrieve structured public YouTube transcripts, captions, comments, channel or video metadata, playlists, and search results through Crawlora for research and summarization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube URLs, search terms, and request parameters are sent to Crawlora with the user's API key.

Mitigation: Install only when this data sharing is acceptable, review Crawlora service terms, and avoid sending sensitive or private inputs.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in unsafe command arguments.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not commit it, and use the bundled helper that sends the key through a temporary curl config.

Risk: Undocumented or unrelated API routes could broaden the helper's behavior beyond the YouTube research use case.

Mitigation: Use only the documented YouTube endpoints; the helper restricts methods and paths to the skill catalog.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public YouTube data from Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
