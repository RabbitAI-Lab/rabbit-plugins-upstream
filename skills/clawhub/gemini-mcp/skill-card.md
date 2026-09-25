## Description:

gemini-mcp helps agents generate and edit images, video, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure and call a Gemini MCP server for media generation workflows, including image creation and editing, video generation, and music generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Gemini API key and may send selected prompts or media to Gemini or a configured hosted service.

Mitigation: Install only when that data flow is acceptable, avoid sensitive prompts or media unless approved, and use appropriately scoped credentials.

Risk: File uploads, deletion, local file paths, URLs, and clipboard inputs can expose unintended media or files.

Mitigation: Use explicit file paths or URLs, review confirmation previews before approving file operations, and avoid clipboard input unless the current clipboard contents are known.

Risk: The runtime package is installed from npm or source outside NVIDIA control.

Mitigation: Pin or review the npm package or source before deployment, and follow the security guidance from the release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package: @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Source repository declared by artifact](https://github.com/chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON configuration snippets, tool-call examples, shell commands, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image, video, and audio files through the configured Gemini MCP server.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
