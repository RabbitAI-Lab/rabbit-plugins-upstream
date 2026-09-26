## Description:

Helps agents generate and edit images, create short videos, and compose music with Google Gemini through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate, revise, and reuse image, video, and music assets through Gemini-backed tools, including workflows that use reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to Gemini or a hosted deployment.

Mitigation: Avoid sensitive photos or documents and review confirmation previews before uploading local files.

Risk: An API credential and reusable uploaded files need care.

Mitigation: Use a dedicated Gemini API key and delete reusable uploads when no longer needed.

Risk: Generated media may be saved in an unexpected local directory.

Mitigation: Set GEMINI_OUTPUT_DIR to a directory you expect.

## Reference(s):

- [ClawHub gemini-mcp release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown with MCP tool-call and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results can provide local paths to generated image, video, and audio files.]

## Skill Version(s):

2.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
