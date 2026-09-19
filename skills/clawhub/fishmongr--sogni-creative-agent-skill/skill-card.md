## Description:

Agent skill and CLI guidance for generating and editing images, videos, music, speech, 3D assets, LoRAs, personas, and durable creative workflows through Sogni AI's decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fishmongr](https://clawhub.ai/user/fishmongr)

### License/Terms of Use:

MIT

## Use Case:

Developers, creative operators, and agent users use this skill to plan and run Sogni media-generation workflows from an agent, including prompt-based generation, image and video editing, music and speech output, personal LoRAs, personas, saved memories, and hosted multi-step workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores persona, memory, personality, and last-render state that can influence later hosted model behavior.

Mitigation: Keep ~/.config/sogni private and periodically inspect or clear saved memories, personality, personas, and render state.

Risk: The skill uses a Sogni API key and may upload selected local media to hosted Sogni services.

Mitigation: Use it only with credentials and media approved for Sogni processing, and protect the SOGNI_API_KEY and ~/.config/sogni credentials file.

Risk: Self-update and no-confirm-cost flows can change installed code or proceed without an interactive cost confirmation.

Mitigation: Run self-update or --no-confirm-cost only after explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fishmongr/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [Sogni Creative Agent Skill npm package](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)
- [Hosted Sogni Intelligence API Modes](references/hosted-api.md)
- [Model Catalog & Sizing Rules](references/models.md)
- [Image Prompt Authoring Guide](references/image-prompting.md)
- [Video Prompting Guide](references/video-prompting.md)
- [Personal LoRAs](references/personal-loras.md)
- [Personas, Memory & Personality](references/personas-memory.md)
- [SAM 3 object selection](references/object-selection.md)
- [Loop Maker](references/loop-maker.md)
- [OpenClaw Plugin Configuration](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, files]

**Output Format:** [Markdown guidance with CLI commands and generated media file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files may include images, videos, audio, speech, masks, 3D models, JSON records, and local configuration or persona state.]

## Skill Version(s):

3.51.1 (source: frontmatter and changelog, released 2026-09-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
