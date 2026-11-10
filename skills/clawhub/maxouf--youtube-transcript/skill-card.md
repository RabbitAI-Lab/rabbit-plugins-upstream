## Description:

Get transcripts of YouTube videos, Shorts, channels, and playlists as timestamped segments, plain text, SRT, or WebVTT, with language and video metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxouf](https://clawhub.ai/user/maxouf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve captions for individual YouTube videos or batches from channels and playlists, then receive transcripts in a requested format or use them as the basis for a summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source URLs and transcript results may be processed remotely by Apify and stored in its datasets.

Mitigation: Before using the Apify routes, review the applicable access and retention settings and avoid sensitive or unlisted sources unless those settings are acceptable.

Risk: The security scan was incomplete because a referenced local path was not found, so it did not establish that every related artifact was reviewed.

Mitigation: Review the full skill and its referenced files before deployment, and consider the scan result incomplete.

## Reference(s):

- [Skill homepage](https://github.com/maxouf/sherwood-skills/tree/main/skills/youtube-transcript)
- [Apify MCP integration](https://mcp.apify.com/?tools=sherwood/youtube-transcript-batch)
- [ClawHub release page](https://clawhub.ai/maxouf/skills/youtube-transcript)

## Skill Output:

**Output Type(s):** [Text, JSON, SRT, WebVTT, Shell commands, Guidance]

**Output Format:** [Transcript text or timestamped JSON, SRT, and WebVTT, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include video and caption metadata, per-video status and errors, and one file per video or a batch dataset.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
