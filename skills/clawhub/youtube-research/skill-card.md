## Description:

Pulls structured YouTube data -- video and channel details, transcripts/captions, comments, playlists, and search -- via the Crawlora API as clean JSON, with no yt-dlp or HTML scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve public YouTube transcripts, captions, comments, channel details, playlist data, and search results as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube URLs, IDs, search queries, and the Crawlora API key are sent to Crawlora when the helper is used.

Mitigation: Use the skill for public YouTube research only, keep the API key in the environment, and avoid submitting sensitive private context as query parameters.

Risk: Requests outside the documented YouTube route set could expose unintended account or API surfaces.

Mitigation: Use the bundled helper, which fixes the Crawlora API base, allows only GET requests, and restricts calls to documented YouTube routes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; the helper is GET-only and limited to documented public YouTube lookup routes.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
