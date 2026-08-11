## Description:

Pulls structured YouTube video, channel, transcript, caption, comment, playlist, and search data through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public YouTube transcripts, captions, comments, video metadata, channel details, playlists, and search results for research, summarization, sentiment analysis, and content discovery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper can send CRAWLORA_API_KEY to an overridden CRAWLORA_API_BASE endpoint.

Mitigation: Use the skill only with CRAWLORA_API_BASE unset or set to a trusted endpoint, and keep the API key in the environment rather than prompts or files.

Risk: The helper supports non-YouTube Crawlora paths even though the skill is presented as a YouTube research skill.

Mitigation: Restrict agent workflows to the documented YouTube endpoints unless broader Crawlora API access is intentionally approved.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are public YouTube data returned by Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
