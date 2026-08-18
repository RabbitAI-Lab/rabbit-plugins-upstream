## Description:

Pulls structured YouTube data, including video and channel details, transcripts, captions, comments, playlists, and search results, via the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to retrieve public YouTube transcripts, captions, comments, channel and video metadata, playlists, and search results for summarization, sentiment review, channel digests, and research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths and send arbitrary request bodies with the user's API key.

Mitigation: Review requested paths and payloads before execution; use a Crawlora key that is acceptable for this skill and prefer documented YouTube endpoints.

Risk: Queries, YouTube URLs, comments, and request bodies are sent to the external Crawlora API.

Mitigation: Avoid sensitive queries or payloads and use the skill for public YouTube data only.

## Reference(s):

- [YouTube endpoint reference](reference/endpoints.md)
- [Crawlora service](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Crawlora API responses are returned as raw JSON for optional jq processing.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
