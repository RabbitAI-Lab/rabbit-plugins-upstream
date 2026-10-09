## Description:

Helps agents generate and edit images, create short videos, and produce music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to direct an agent to generate or refine images, videos, and music from prompts and supplied media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, media, clipboard images, URLs, and base64 data may be sent to Gemini or a hosted service.

Mitigation: Use only content you are authorized to share; avoid sensitive or regulated data without consent and a review of service retention.

Risk: Use requires a Gemini API key and media generation may incur charges.

Mitigation: Install only from a trusted package source, safeguard the API key, and review billing before generation.

## Reference(s):

- [gemini-mcp ClawHub release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [gemini-mcp npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [PNG or JPEG images, MP4 video, MP3 audio, and text responses with file paths and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files may be saved locally or returned inline; responses can include job IDs for asynchronous generation.]

## Skill Version(s):

2.3.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
