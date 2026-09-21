## Description:

Pulls structured YouTube data -- video and channel details, transcripts/captions, comments, playlists, and search -- via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to retrieve public YouTube transcripts, captions, comments, video/channel metadata, playlists, and search results through Crawlora for summaries, sentiment review, channel digests, and research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested YouTube identifiers, search terms, and the Crawlora API key to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode, commit, or pass the key in query parameters.

Risk: The helper is intended for public YouTube research requests only.

Mitigation: Use the documented helper for public YouTube lookups and avoid submitting sensitive or private research terms unless approved for use with Crawlora.

## Reference(s):

- [youtube-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/youtube-research)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and limits helper requests to documented public YouTube GET endpoints.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
