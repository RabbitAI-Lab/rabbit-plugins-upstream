## Description:

gemini-mcp helps agents generate and edit images, short videos, and music with Google Gemini models through a registered MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an assistant to Gemini-powered media generation and editing workflows for images, video, and music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned third-party MCP package with a Gemini API key.

Mitigation: Review the package source, pin a trusted version before installing, and use a dedicated restricted Gemini API key.

Risk: Project MCP configuration or environment files may expose Gemini API credentials if committed.

Mitigation: Do not commit `.mcp.json` or `.env` files containing secrets; manage credentials through approved secret storage.

Risk: File, clipboard, and hosted-upload paths can send local media or clipboard contents to Gemini or a hosted upload service.

Mitigation: Provide only media files or clipboard contents that are intended for that service and avoid sensitive inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets; tool results can include generated media file paths and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media workflows can produce image, video, and audio files; some calls support async job IDs, inline bytes, or reusable file references.]

## Skill Version(s):

1.14.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
