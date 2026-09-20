## Description:

gemini-mcp helps agents set up and use a Gemini MCP server to generate and edit images, videos, and music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure the @chrischall/gemini-mcp package and call Gemini-powered MCP tools for image generation, image editing, video generation, music generation, file upload, and iterative media refinement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to Gemini or a configured hosted endpoint.

Mitigation: Use only trusted deployments and avoid sending sensitive personal, business, or confidential media unless upload, billing, retention, and local-output behavior are understood.

Risk: The skill can upload local files, URLs, or base64 media to external services and may write generated media files locally.

Mitigation: Review selected input files and output directories before use, prefer reusable file URIs over repeated base64 uploads, and delete temporary uploads when they are no longer needed.

Risk: Generated media can contain model errors, including incorrect rendered text or unexpected edits.

Mitigation: Inspect generated images, videos, and music before publication or downstream use, especially when outputs include text, branding, or factual claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with JSON configuration, shell commands, MCP tool calls, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include PNG/JPEG images, MP4 videos, MP3 audio, Gemini Files API file URIs, async job status, and local file paths depending on the selected MCP tool.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
