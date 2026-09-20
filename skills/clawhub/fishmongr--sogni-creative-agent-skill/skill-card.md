## Description:

Generate and edit images, video, music, speech, 3D assets, upscales, personas, and multi-step creative workflows using Sogni AI's decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fishmongr](https://clawhub.ai/user/fishmongr)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and external users use this skill to plan and run Sogni creative media workflows from an agent, including generation, editing, upscaling, media analysis, personas, and hosted durable workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be sent to Sogni services during hosted or durable workflows.

Mitigation: Use direct CLI mode for private media that should not be uploaded to hosted durable workflows.

Risk: The skill stores a Sogni API key and creative preferences in local configuration paths.

Mitigation: Store credentials with restricted file permissions and install only in environments where local Sogni state is acceptable.

Risk: Media generation and long workflows can incur model or provider costs.

Mitigation: Review cost settings and estimates before starting long or multi-step workflows.

Risk: Optional self-update tooling changes the installed CLI.

Mitigation: Run self-updates only when intentionally upgrading the installed Sogni CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fishmongr/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [Hosted API guide](references/hosted-api.md)
- [Model guide](references/models.md)
- [Video prompting guide](references/video-prompting.md)
- [Image prompting guide](references/image-prompting.md)
- [Video editing guide](references/video-editing.md)
- [Object selection guide](references/object-selection.md)
- [OpenClaw configuration guide](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, JSON plans, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce image, video, audio, 3D model, JSON, and workflow artifacts through Sogni CLI and API calls.]

## Skill Version(s):

3.52.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
