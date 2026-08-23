## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and invoke a Gemini MCP server for image generation and editing, short video generation, and music or audio clip generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Gemini API key and may send prompts and selected media inputs to Google Gemini.

Mitigation: Install only when that data flow is acceptable, protect the API key, and review or pin the npm package in controlled environments.

Risk: Clipboard, broad input directory, file path, URL, and local output behaviors can expose sensitive media or files if used carelessly.

Mitigation: Prefer explicit file paths or URLs, avoid from_clipboard and broad GEMINI_INPUT_DIR settings for sensitive content, and set output_dir or inline behavior intentionally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of local media files through the configured Gemini MCP server.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
