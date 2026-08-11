## Description:

Omni Reader helps agents parse PDFs, Office files, images, scans, webpages, audio, video, and archives into Markdown or clean text through Cue MCP and HTTP API integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure Omni Reader for converting local files or HTTPS URLs into Markdown, clean text, hypertext, or chunks for downstream agent workflows and programmatic ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, media, URLs, and extracted content may be sent to Cue/IIIS remote infrastructure.

Mitigation: Use the skill only for data you are comfortable sending to that infrastructure, and avoid highly confidential material until the publisher clarifies upload, processing, storage, retention, and deletion behavior.

Risk: The evidence reports inconsistent privacy and data-flow claims around remote parsing and local bridge behavior.

Mitigation: Review current publisher terms and deployment behavior before organizational rollout, and require user confirmation before parsing local or sensitive files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Cue Omni Reader web app](https://cuecue.cn/hub/omni-reader)
- [Cue API key portal](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, bash, and Python examples; the parsing service returns markdown, hypertext, chunks, or clean text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-file parsing up to 256 MiB; supports HTTPS URLs and local files through an optional Node.js bridge.]

## Skill Version(s):

1.2.1 (source: evidence.release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
