## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to configure and call a Gemini MCP server for image generation, image editing, consistent image sets, short video generation, and music or audio clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned third-party MCP package that receives a Gemini API key and local file access.

Mitigation: Review the npm package before installing, pin it to a specific audited version, and prefer a project-scoped MCP configuration.

Risk: Gemini API credentials and local media paths could be exposed or used beyond the intended project scope.

Mitigation: Use a dedicated Gemini API key with quotas, avoid storing broad credentials in shared project files, and set explicit input and output directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Code, Files]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference generated image, video, music, and upload files through the configured MCP server.]

## Skill Version(s):

1.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
