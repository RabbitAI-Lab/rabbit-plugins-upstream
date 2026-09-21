## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Gemini MCP server for generating or editing images, creating short videos, composing music, and managing media inputs for Gemini generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Gemini API key and uses a third-party MCP package.

Mitigation: Install only after reviewing and trusting the @chrischall/gemini-mcp package, and provide a scoped Gemini API key through environment configuration rather than embedding credentials in prompts or files.

Risk: Local paths, clipboard images, URLs, base64 media, or uploaded files may be sent to Gemini or a configured hosted endpoint and may incur billing.

Mitigation: Review each media input before use, avoid sensitive files, prefer reusable file references over repeated base64 payloads, and confirm billing expectations before running generation tasks.

Risk: Uploaded media may persist temporarily in Gemini Files API storage.

Mitigation: Use deletion workflows for uploads that should be removed before their normal expiry and avoid uploading confidential media unless retention is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [@chrischall/gemini-mcp npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to write generated media files or call Gemini MCP tools that return file paths and metadata.]

## Skill Version(s):

2.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
