## Description:

Pulls structured YouTube data, including video and channel details, transcripts, captions, comments, playlists, and search results, via the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to retrieve public YouTube transcripts, captions, comments, channel data, playlists, video metadata, and search results for summaries, sentiment analysis, channel digests, and research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to a host controlled by CRAWLORA_API_BASE.

Mitigation: Run it only with the default Crawlora API base or a trusted value, and rotate the key if it was used with an unexpected base.

Risk: The helper script can call paths beyond the documented YouTube endpoints.

Mitigation: Restrict usage to the documented /youtube endpoints when using this skill for YouTube research.

Risk: YouTube queries, video IDs, and related request data are shared with Crawlora.

Mitigation: Use the skill only for data you are comfortable sending to Crawlora, and prefer a limited or disposable Crawlora API key.

## Reference(s):

- [YouTube endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/youtube-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API calls use the x-api-key header and may use CRAWLORA_API_BASE if set.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
