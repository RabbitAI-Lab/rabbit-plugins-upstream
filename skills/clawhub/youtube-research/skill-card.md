## Description:

Pulls structured YouTube data — video and channel details, transcripts/captions, comments, playlists, and search — via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and analysts use this skill to find public YouTube videos and retrieve video, channel, transcript, comment, and playlist data for summaries and bounded research. It can help ground themes and claims in timestamped transcript segments while noting when captions are unavailable or may be inaccurate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and requested YouTube identifiers are sent to Crawlora, and successful requests can consume API credits.

Mitigation: Avoid sensitive search terms and account for credit usage before making requests.

Risk: The API key could be exposed if handled insecurely.

Mitigation: Keep CRAWLORA_API_KEY in the environment; do not hardcode it, pass it in a query parameter, or commit it.

## Reference(s):

- [Crawlora API setup and key](https://crawlora.net)
- [YouTube endpoint reference](artifact/reference/endpoints.md)
- [ClawHub release page](https://clawhub.ai/crawlora-org/skills/youtube-research)

## Skill Output:

**Output Type(s):** [JSON data, Text analysis, Markdown]

**Output Format:** [Normalized JSON results and concise text or Markdown research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript-based claims can be tied to timestamps; captions may be unavailable or inaccurate.]

## Skill Version(s):

1.0.21 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
