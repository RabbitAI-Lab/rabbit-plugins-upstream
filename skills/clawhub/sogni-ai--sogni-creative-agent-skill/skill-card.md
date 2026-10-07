## Description:

Enables agents to generate and edit images, videos, music, speech, and 3D assets using Sogni AI's creative tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to direct an agent to generate or edit images, video, music, speech, and 3D media, and to manage reusable creative preferences and workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local reference media may be uploaded for hosted generation.

Mitigation: Confirm what media will be sent to Sogni before using hosted modes.

Risk: Paid or external-vendor models can consume credits.

Mitigation: Review model and billing choices before running costly jobs.

Risk: API credentials and optional personas, memories, MCP registration, or updates can persist beyond the session.

Mitigation: Protect the API key and use the documented uninstall or data-clearing steps when persistent state is no longer wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Model and media guide](references/models.md)
- [Hosted API guide](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Media files]

**Output Format:** [Markdown guidance and generated image, video, audio, or 3D files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation requires a Sogni API key and may consume paid credits.]

## Skill Version(s):

3.55.0 (source: server release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
