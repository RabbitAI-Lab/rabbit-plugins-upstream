## Description:

Search YouTube and retrieve videos, shorts, comments, transcripts, streams, and channel data as structured JSON across video and channel endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search YouTube and retrieve structured video, transcript, comment, stream, and channel data through Scavio endpoints. It is suited for content research, metadata lookup, transcript retrieval, and channel analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for all documented API calls.

Mitigation: Keep SCAVIO_API_KEY out of source control and load it from an environment variable or secret store.

Risk: Broad pagination, transcript retrieval, search, shorts, and stream requests can consume credits quickly.

Mitigation: Check credit usage before large requests and avoid unnecessary pagination or transcript calls.

Risk: Using an optional package can expand the local dependency footprint.

Mitigation: Prefer the direct HTTPS examples or a virtual environment when the LangChain package is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/youtube-data-api)
- [Scavio documentation](https://scavio.dev/docs)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=youtube-data-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python examples, and structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio HTTPS endpoints; API responses include credit usage and remaining credit fields.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
