## Description:

Guides agents in generating and editing images, videos, and music through a Google Gemini MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or edit images, create short videos, and produce music with Gemini models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to external services, with potential retention and billing implications.

Mitigation: Use only media you are comfortable sharing under the provider's terms, and review expected costs before generation.

Risk: Uploading local files or deleting uploaded media can affect user data.

Mitigation: Review the file or deletion preview and obtain user approval before confirming the action.

## Reference(s):

- [ClawHub gemini-mcp release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, MCP tool calls]

**Output Format:** [Markdown with configuration and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connected service can save generated images, videos, and audio files.]

## Skill Version(s):

2.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
