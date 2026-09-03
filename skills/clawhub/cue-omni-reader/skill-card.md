## Description:

Omni Reader guides agents to parse documents, images, audio, video, web pages, and archives into Markdown or clean text through Cue's MCP/API service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to configure Cue Omni Reader for document and multimodal file parsing, including OCR, ASR, video understanding, and conversion of supported sources to Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local-file privacy claims conflict with the remote-service architecture described for parsing.

Mitigation: Avoid confidential local documents until the publisher clarifies whether local Bridge file contents are uploaded, retained, or processed locally.

Risk: Remote URL/API mode sends parsing requests to Cue infrastructure.

Mitigation: Use only sources approved for third-party processing and review Cue service terms and retention behavior before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Publisher Profile](https://clawhub.ai/user/panting09266-ai)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API Key](https://cuecue.cn/hub/api-key)
- [Cue MCP Catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, curl, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs parsing workflows that can return Markdown, hypertext, chunks, status, outlines, and saved result files.]

## Skill Version(s):

1.2.8 (source: server release metadata; artifact frontmatter says 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
