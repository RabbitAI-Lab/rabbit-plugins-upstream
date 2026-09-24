## Description:

Generate and edit images, video, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to configure and call a Gemini MCP server for media generation workflows, including image generation and editing, short video creation, and music or audio clip generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided media may be uploaded to Gemini or the configured hosted service.

Mitigation: Use the skill only with media intended for that service, avoid private clipboard contents unless deliberately selected, and prefer reusable file references when available.

Risk: The skill requires a Gemini API key.

Mitigation: Keep the API key scoped and protected as a secret, and avoid committing it to project files or sharing it in chat.

Risk: Generated media can contain incorrect details, including mis-rendered text or other model artifacts.

Mitigation: Review generated images, videos, and audio before publication or downstream use, especially when text, brands, or factual details matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool-call patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The configured MCP server may create media files and may upload selected user media to Gemini or a hosted service.]

## Skill Version(s):

2.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
