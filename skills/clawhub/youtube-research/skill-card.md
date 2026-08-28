## Description:

Pulls structured YouTube data, including video and channel details, transcripts, captions, comments, playlists, and search results, through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve structured public YouTube transcripts, metadata, comments, playlists, channel data, and search results for summarization, sentiment analysis, and research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths and methods, which is broader than the stated YouTube-only purpose.

Mitigation: Review before installing and restrict use to approved /youtube/* endpoints, or narrow the helper script before deployment.

Risk: The skill uses an authenticated Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid hardcoding or committing it, and rotate the key if it is exposed.

## Reference(s):

- [YouTube endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API provider](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/youtube-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; API responses are intended to contain public YouTube data.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
