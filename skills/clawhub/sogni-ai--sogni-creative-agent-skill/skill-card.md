## Description:

Helps agents generate and edit images, video, music, voice, and 3D assets using Sogni AI services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill with an AI agent to generate and edit media, upscale images and video, and organize reusable personas and creative workflows through Sogni.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using remote generation requires a Sogni API key and may send selected media to Sogni for processing.

Mitigation: Provide the key only when needed and review media before submitting it to Sogni.

Risk: Sogni-specific personas and memories are stored locally.

Mitigation: Protect local Sogni data and use the documented purge or uninstall procedure carefully, after backing up anything you want to keep.

Risk: Self-update prompts may change the installed skill or its dependencies.

Mitigation: Review update prompts before authorizing an update.

## Reference(s):

- [Sogni Creative Agent Skill on ClawHub](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Model guide](artifact/references/models.md)
- [Personas and memory guide](artifact/references/personas-memory.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return JSON result metadata and produce image, video, audio, and 3D files through Sogni.]

## Skill Version(s):

3.58.2 (source: ClawHub release metadata, SKILL.md, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
