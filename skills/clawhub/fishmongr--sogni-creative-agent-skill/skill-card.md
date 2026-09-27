## Description:

Helps agents create and edit images, video, music, speech, and 3D assets using Sogni AI's media-generation services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fishmongr](https://clawhub.ai/user/fishmongr)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to direct an agent to generate or transform visual and audio media, manage creative references and personas, and coordinate multi-step Sogni workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and generation contact npm and Sogni and require a Sogni API key.

Mitigation: Review network access before installation and keep the API key private.

Risk: Hosted workflows upload referenced local media to Sogni.

Mitigation: Use direct CLI mode for private media that should not leave the machine.

Risk: Hosted creative workflows may incur charges.

Mitigation: Keep cost confirmation and workflow cost ceilings enabled.

Risk: Personas and memories persist locally; self-update and uninstall or purge can change installed software or remove stored data.

Mitigation: Review stored data and run update or removal commands only when explicitly intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fishmongr/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Hosted API guide](artifact/references/hosted-api.md)
- [Model guide](artifact/references/models.md)
- [Sogni pricing](https://docs.sogni.ai/pricing/#spark-packs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance, command output, and generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media may include images, videos, audio, and 3D assets.]

## Skill Version(s):

3.54.0 (source: SKILL.md metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
