## Description:

Routes image, video, and audio generation requests to suitable dLazy CLI models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose dLazy CLI commands for generating or editing images, video, and audio from prompts and optional media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media may leave the device for dLazy's hosted service.

Mitigation: Review inputs and confirm before uploading private media files.

Risk: Global installation and CLI login can persist a local executable and API key.

Mitigation: Use the pinned npx invocation and DLAZY_API_KEY if you prefer to avoid a persistent global CLI or saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI package (listed in metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses contain JSON with generated media URLs.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
