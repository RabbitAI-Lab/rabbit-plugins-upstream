## Description:

Search YouTube and retrieve videos, shorts, comments, transcripts, streams, and channel data as structured JSON. 15 endpoints across video and channel surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to search YouTube and retrieve structured video, comment, transcript, stream, and channel data through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using this skill need access to a Scavio API key.

Mitigation: Provide SCAVIO_API_KEY through a secret or environment variable and avoid logging or embedding the key in generated code.

Risk: Paginated lookups, transcripts, and stream lookups can consume Scavio credits quickly.

Mitigation: Confirm scope before broad pagination and tell the user when higher-cost endpoints such as transcripts or streams are being used.

Risk: YouTube lookup inputs are sent to Scavio's API.

Mitigation: Use the skill only for lookup inputs that are appropriate to share with Scavio's service.

Risk: Default language and region behavior may not match the user's intent.

Mitigation: Specify language or region explicitly when English or US defaults are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/youtube-data-api)
- [Scavio documentation](https://scavio.dev/docs)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=youtube-data-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions, Python examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON and may consume Scavio credits.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
