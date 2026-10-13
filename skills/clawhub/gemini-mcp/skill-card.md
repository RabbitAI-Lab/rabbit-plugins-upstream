## Description:

Guides an agent in generating and editing images, video, and music through a Google Gemini MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to create or refine images, short videos, and music with Gemini-powered tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external MCP package requires trusting its publisher.

Mitigation: Review or pin @chrischall/gemini-mcp before use and install only if you trust the publisher.

Risk: Prompts and selected media are sent to Gemini or a configured hosted deployment; uploaded files may be retained temporarily.

Mitigation: Do not send private media unless remote processing and temporary retention are acceptable.

Risk: API credentials or unintended clipboard images could be exposed during use.

Mitigation: Protect GEMINI_API_KEY and use clipboard input only after checking the copied image.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)

## Skill Output:

**Output Type(s):** [Guidance, MCP tool calls]

**Output Format:** [Markdown guidance and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images, videos, and music can be saved as media files or returned inline where supported.]

## Skill Version(s):

2.3.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
