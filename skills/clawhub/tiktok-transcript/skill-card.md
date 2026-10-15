## Description:

Turns supported video links into transcripts, on-screen text, key points, and video metadata for an agent to share or summarize.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users extract speech and on-screen text from supported public videos, then share the transcript, a summary, or a translation. A keyless request returns a limited summary; full transcripts require an API key and usage credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links or share text are sent to LinkDigest for processing and may be cached by link.

Mitigation: Avoid private links and sensitive share text; submit only content suitable for remote processing and caching.

Risk: An API key grants access to usage credits, and unpinned MCP tooling may receive the bearer token.

Mitigation: Keep the key out of chat and code, set appropriate credit limits, and prefer the provided Python client or pinned, trusted MCP tooling.

Risk: Automatic transcription and model-generated video text may contain mistakes or approximate timestamps.

Mitigation: Check quotations, names, numbers, and timestamps against the original video before relying on them.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API reference](https://linkdigest.dev/openapi.json)
- [LinkDigest API keys](https://linkdigest.dev/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON, with optional natural-language summaries or translations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full results may include segment-level timestamps, on-screen text, video metadata, credit use, and partial-read indicators; keyless access returns a limited summary.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
