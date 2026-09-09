## Description:

A comprehensive generation skill that helps an agent generate images, videos, and audio by selecting and invoking the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route multimodal media-generation requests to dLazy CLI commands for image, video, audio, speech, music, segmentation, enhancement, and format-conversion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files may be sent to dLazy cloud services for generation.

Mitigation: Use the skill only for content intended for dLazy processing, and avoid sensitive prompts or private media unless cloud upload is acceptable.

Risk: The dLazy CLI may store an API key in a local user configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY or revoke/remove ~/.dlazy/config.json after use on shared systems.

Risk: Using a global install persists a third-party CLI on the system.

Mitigation: Prefer npx or a contained environment for one-off runs when persistent installation is not needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides command selection and may produce or consume dLazy-hosted media URLs returned by the CLI.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
