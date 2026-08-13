## Description:

Gemini MCP lets agents generate and edit images, short videos, and music through Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to connect an agent to Gemini media-generation tools for image generation, image editing, consistent image sets, short video generation, and music or audio clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to Google Gemini services.

Mitigation: Use the skill only for content that may be processed by Google Gemini services, and avoid sending sensitive prompts or media unless that transfer is acceptable.

Risk: The from_clipboard option can use the current macOS clipboard image.

Mitigation: Prefer explicit file paths or uploaded file URIs for sensitive reference images, and confirm clipboard contents before enabling clipboard-based input.

Risk: Unpinned npx installation can resolve to a newer npm package version later.

Mitigation: Pin the npm package version in MCP configuration when repeatable installs are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to call MCP tools that save generated PNG, JPEG, MP4, MP3, or WAV files, return file paths, or return inline media metadata.]

## Skill Version(s):

1.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
