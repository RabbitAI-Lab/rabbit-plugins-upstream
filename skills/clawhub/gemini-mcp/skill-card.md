## Description:

Generates and edits images, video, and music with Google Gemini models through a configured Gemini MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Gemini MCP server for media generation workflows, including image creation and editing, consistent image sets, short videos, and music/audio clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party MCP package receives a Gemini API key and may send prompts, selected files, URLs, or copied clipboard images to Gemini.

Mitigation: Install only when that data flow is acceptable for the intended use, scope the API key appropriately, and avoid sending sensitive prompts or media.

Risk: Clipboard and local-file input paths can expose unintended media if used carelessly.

Mitigation: Use from_clipboard only immediately after copying the intended image, pass explicit file paths, and delete uploaded files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Files, API Calls]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, MCP tool calls, and generated media file paths or inline media responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved as PNG or JPEG depending on the tool path; videos are saved as MP4; music is saved as MP3 or WAV when supported.]

## Skill Version(s):

1.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
