## Description:

Generates and edits images, video, and music using Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images, create short videos, and compose music from prompts or supplied media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package or exposing a Gemini API key in the MCP environment.

Mitigation: Confirm that you trust the @chrischall/gemini-mcp package before installing it, and protect the API key.

Risk: Supplied photos, videos, audio, clipboard contents, or upload-folder files may be sent to Gemini-related services and retained temporarily.

Mitigation: Only provide media and grant access to folders when that data flow and temporary retention are acceptable.

## Reference(s):

- [ClawHub gemini-mcp listing](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Text]

**Output Format:** [PNG or JPEG images, MP4 videos, MP3 audio, and tool-result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media can be saved to disk or returned inline; results may include file paths and generation metadata.]

## Skill Version(s):

2.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
