## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to configure and operate a Gemini MCP server for image generation and editing, consistent image sets, short video generation, and music or audio clip generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party MCP package and a Gemini API key.

Mitigation: Install only after accepting the third-party package dependency and store the Gemini API key in the configured environment rather than in prompts or shared files.

Risk: Prompts and selected reference media may be sent to Gemini for generation or editing.

Mitigation: Use the skill only with prompts and media that are appropriate to share with the Gemini service.

Risk: Clipboard input can upload unintended image content if the clipboard contains the wrong item.

Mitigation: Use clipboard input only after confirming the clipboard contains the intended image.

Risk: Uploaded reference files may remain available until their service expiry.

Mitigation: Use the delete-file tool for uploaded references that should not be retained until expiry.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, tool-call results, and generated media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may include images, MP4 video, MP3 audio, or WAV audio depending on the selected Gemini tool and model.]

## Skill Version(s):

1.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
