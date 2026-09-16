## Description:

Pulls structured YouTube data - video and channel details, transcripts/captions, comments, playlists, and search - via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to retrieve public YouTube transcripts, captions, comments, playlists, channel data, video metadata, and search results through the Crawlora API for summaries, sentiment review, channel digests, and research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube URLs, video or channel IDs, search terms, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill for public YouTube research and avoid sending private prompts, secrets, or unrelated sensitive data in query parameters or POST bodies.

Risk: The API key could be exposed if hardcoded, committed, or placed directly in command-line arguments.

Mitigation: Keep the key in CRAWLORA_API_KEY and use the helper script, which sends the key through a temporary curl config rather than as a command-line argument.

Risk: Some YouTube videos may not expose captions or transcripts.

Mitigation: Check the transcript languages endpoint before relying on transcript output and handle empty transcript responses in downstream summaries or analyses.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/youtube-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API for documented YouTube endpoints.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
