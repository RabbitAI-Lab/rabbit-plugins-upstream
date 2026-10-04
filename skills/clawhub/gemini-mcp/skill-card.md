## Description:

Helps agents generate and edit images, create short videos, and compose music with Google Gemini media tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or refine images, video clips, and music from prompts or supplied media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied prompts and media may be sent to Gemini or a hosted deployment.

Mitigation: Use non-sensitive test media first and approve local-file or clipboard uploads explicitly.

Risk: The required third-party package and Gemini API key introduce software and credential exposure.

Mitigation: Review the package before running it and keep the API key scoped and protected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key setup](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, API calls]

**Output Format:** [Text guidance and MCP tool calls; generated image, video, or audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media may be saved to disk or returned inline, depending on the tool and settings.]

## Skill Version(s):

2.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
