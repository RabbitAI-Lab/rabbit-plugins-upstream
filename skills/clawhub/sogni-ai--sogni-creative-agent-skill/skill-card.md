## Description:

Helps agents create and edit images, video, music, and speech through Sogni AI, including upscaling and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to direct an agent to generate, edit, and upscale media with Sogni services, or to coordinate multi-step creative projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill connects to Sogni services with a Sogni API key.

Mitigation: Install only if service access is intended, and keep the API key protected.

Risk: Hosted workflows upload local media to Sogni storage.

Mitigation: Use direct CLI mode for private media that should not be uploaded through hosted workflows.

Risk: Self-updates can change the installed skill and runtime.

Mitigation: Review any self-update prompt before approving it.

Risk: Uninstall with purge removes local Sogni data, including credentials, after creating a backup.

Mitigation: Review the backup and retain needed data before purging.

## Reference(s):

- [Sogni Creative Agent Skill on ClawHub](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Hosted API guide](references/hosted-api.md)
- [Video prompting guide](references/video-prompting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Conversational text and Markdown, including CLI commands and media result links or paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sogni generation jobs may return links or paths to image, video, audio, or 3D assets.]

## Skill Version(s):

3.58.0 (source: release metadata, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
