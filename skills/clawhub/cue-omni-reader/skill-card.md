## Description:

Cue Omni Reader is a multimodal document-parsing integration that sends files, URLs, images, scanned documents, office files, web pages, audio, video, and archives to Cue remote MCP or HTTP services and returns Markdown or related parsed text formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure Cue Omni Reader through MCP or HTTP APIs and parse multimodal documents into Markdown, clean text, hypertext, or chunks. It is suited to workflows that need OCR, ASR, visual understanding, and broad document format coverage through Cue-hosted services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found contradictory local-file privacy statements that could mislead users about whether confidential local documents are uploaded to Cue-controlled services.

Mitigation: Treat local-file parsing as remote processing; use only files approved for that service, prefer URL-only workflows or a local parser for confidential documents, and review the publisher's corrected privacy wording before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Cue Omni Reader web app](https://cuecue.cn/hub/omni-reader)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue MCP service catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code, markdown, text]

**Output Format:** [Markdown documentation with JSON, bash, curl, and Python snippets; the configured parser service returns Markdown, clean text, hypertext, or chunks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key for remote parsing; local-file workflows may require installing the Cue Bridge and sending document content through Cue-controlled parsing infrastructure.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
