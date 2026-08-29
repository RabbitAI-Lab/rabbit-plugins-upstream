## Description:

Generate and edit images, video, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call a Gemini MCP server for media generation, media editing, iterative refinement, file uploads, and model selection. It is intended for image, video, and music workflows that can send prompts and referenced media to Google Gemini services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, referenced images, videos, audio, URLs, or clipboard images may be sent to Google Gemini services through a third-party MCP package.

Mitigation: Avoid sensitive or third-party private media unless permission, privacy expectations, and billing implications are understood.

Risk: Uploaded media or file references can persist temporarily, and generated content may create billing or retention concerns.

Mitigation: Use reusable file references intentionally, delete uploads when no longer needed, and avoid unnecessary uploads of private material.

Risk: Generated media can contain inaccurate details, including mis-rendered text or years.

Mitigation: Review generated outputs before publication or downstream use, especially when visual text, dates, brands, or factual claims matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline JSON and shell commands; MCP calls return saved media file paths and optional metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce images, MP4 video, MP3/WAV audio, file upload references, interaction IDs, and async job IDs depending on the selected tool.]

## Skill Version(s):

1.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
