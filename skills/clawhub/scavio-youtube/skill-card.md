## Description:

Search YouTube and retrieve videos, shorts, comments, transcripts, streams, and channel data as structured JSON. 15 endpoints across video and channel surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search YouTube, retrieve public video and channel data, inspect comments and transcripts, and request stream metadata through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends YouTube lookup requests to Scavio using a user-provided API key.

Mitigation: Install only if that data flow is acceptable and keep SCAVIO_API_KEY out of source control.

Risk: Broad pagination and transcript retrieval can consume Scavio credits quickly.

Mitigation: Monitor credit usage and confirm user intent before large searches, many paginated requests, or transcript retrieval.

Risk: Stream URLs may be sensitive to platform and content usage rules.

Mitigation: Treat stream URLs according to applicable platform, content, and organizational policies.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-youtube)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio YouTube API endpoints that return structured JSON.]

## Skill Version(s):

3.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
