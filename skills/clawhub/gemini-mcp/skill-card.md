## Description:

Generate and edit images, video, and music with Google Gemini models through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can use the skill to generate or edit images, create consistent image sets, and produce video or audio content with Gemini models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Gemini API key may be exposed.

Mitigation: Protect GEMINI_API_KEY and avoid exposing it in shared configuration.

Risk: Uploaded media may be shared with Gemini or the selected hosting service.

Mitigation: Upload only media you intend to share with Gemini and the chosen host.

Risk: API usage can incur charges, and an unpinned server package may change.

Mitigation: Review usage costs and preferably pin the server package version.

Risk: Uploaded media and saved character or style references may be retained.

Mitigation: Review hosting retention terms and delete saved references when no longer needed.

Risk: Local media or deletion actions could be confirmed unintentionally.

Mitigation: Keep user confirmations enabled and use clipboard input intentionally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [Gemini MCP npm package](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API key](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Text metadata]

**Output Format:** [Generated media files, with optional inline media and text metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media format and delivery depend on the selected Gemini tool and options.]

## Skill Version(s):

2.4.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
