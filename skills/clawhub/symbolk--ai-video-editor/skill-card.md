## Description:

Raw assets and requirements in, result video out: edit video with Sparki, the video agent powered by Gemini multimodal AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[symbolk](https://clawhub.ai/user/symbolk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send a local MP4 and editing requirements to the Sparki Business API, then receive a rendered MP4 result after upload, project creation, polling, and download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected MP4 files, prompts, object keys, project IDs, and the Sparki API key to a remote service.

Mitigation: Use only with media and prompts suitable for Sparki processing, avoid sensitive or regulated content, and review Sparki retention and privacy terms before use.

Risk: Weak URL validation around configured API and download endpoints could expose credentials or retrieve files from an unintended host if configuration is changed.

Mitigation: Keep SPARKI_API_URL and SPARKI_API_BASE on trusted HTTPS Sparki endpoints and do not point them at untrusted or plain HTTP services.

Risk: Downloaded render outputs are written to the configured output directory.

Mitigation: Choose and monitor the output directory, and review downloaded files before sharing or using them in downstream workflows.

## Reference(s):

- [Sparki homepage](https://sparki.io)
- [Sparki Business API base URL](https://business-agent-api.sparki.io)
- [ClawHub skill page](https://clawhub.ai/symbolk/skills/ai-video-editor)
- [Publisher profile](https://clawhub.ai/user/symbolk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Python script usage; the runtime workflow downloads an MP4 file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SPARKI_API_KEY and Python; uploads MP4 files and prompts to the Sparki remote service and writes rendered video files to the configured output directory.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
