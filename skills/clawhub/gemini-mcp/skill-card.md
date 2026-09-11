## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a third-party Gemini MCP server for media generation workflows, including image generation and editing, short video generation, and music or audio clip generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run mutable third-party MCP code.

Mitigation: Pin a reviewed package version or source commit before installation and review updates before deploying them.

Risk: The skill requires a Gemini API key.

Mitigation: Use a dedicated restricted API key, keep it outside project files, and exclude credential files from source control.

Risk: Prompts and selected media may be sent to Gemini or a hosted deployment.

Mitigation: Avoid confidential, regulated, or unapproved images, videos, audio, prompts, and clipboard contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Code]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The configured MCP server can produce media files such as images, MP4 video, and MP3 audio.]

## Skill Version(s):

1.14.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
