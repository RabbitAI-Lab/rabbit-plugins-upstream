## Description:

Sogni Creative Agent Skill lets AI agents generate and edit images, videos, music, speech, 3D assets, and multi-step creative workflows through the Sogni AI CLI and decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fishmongr](https://clawhub.ai/user/fishmongr)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to connect an agent runtime to Sogni AI for creative media generation, editing, upscaling, persona-based workflows, and durable multi-step creative plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOGNI_API_KEY and local Sogni state, which can expose account access or user preferences if stored carelessly.

Mitigation: Store credentials in the documented credentials file or environment variable with appropriate file permissions, and review local state under ~/.config/sogni before sharing or purging it.

Risk: Hosted modes can contact Sogni services and upload referenced media.

Mitigation: Use hosted modes only for media that may leave the local machine, and prefer direct CLI modes when private media must remain local.

Risk: Persistent integrations, self-update prompts, and uninstall purge behavior can change local agent configuration or remove local Sogni data.

Mitigation: Review integration registration, self-update, and uninstall commands before approving them; preserve the uninstall backup when purging user data.

Risk: Creative generation can incur usage costs or consume subscription/token balance.

Mitigation: Review cost-confirmation and billing-mode settings before generation, especially for video, hosted workflows, and repeated retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fishmongr/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [npm package](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)
- [Hosted API guide](references/hosted-api.md)
- [Models reference](references/models.md)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Personas and memory guide](references/personas-memory.md)
- [OpenClaw configuration guide](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with CLI commands and JSON workflow/configuration examples; generated media files when commands are executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands normally require SOGNI_API_KEY, Node.js, and optional ffmpeg/ffprobe; final generated files are directed to the user's current working directory unless another path is requested.]

## Skill Version(s):

3.52.2 (source: frontmatter and changelog, released 2026-09-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
