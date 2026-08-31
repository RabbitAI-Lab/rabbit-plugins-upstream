## Description:

Generates and edits images, video, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure an agent to call Gemini media-generation tools for creating, editing, iterating on, and saving images, short videos, and audio clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses a Gemini API key and sends prompts, reference media, and generation requests to Gemini/Google services.

Mitigation: Install only when this data flow is acceptable, avoid sensitive prompts or media unless approved, and manage the API key as a secret.

Risk: Local files, uploaded media, and generated outputs may be saved in the workspace or retained by the Files API for the documented retention window.

Mitigation: Use explicit output directories or inline output when appropriate, track generated file paths, and delete uploaded files when they should not remain available.

## Reference(s):

- [npm package: @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Files, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, tool-call examples, shell commands, generated media file paths, and optional inline media metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved as PNG or JPEG, video as MP4, and audio as MP3 or WAV; inline output can return bytes with metadata.]

## Skill Version(s):

1.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
