## Description:

Image generation skill that selects an appropriate dLazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users use this skill to route image-generation and image-processing requests to the appropriate dLazy CLI model, including text-to-image, image editing, upscaling, segmentation, and vectorization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and local media files supplied to image or media fields may be sent to dLazy hosted services.

Mitigation: Use the skill only for data intended for dLazy processing, and avoid passing private files unless upload is intended.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use the documented per-invocation environment variable or rotate and revoke organization-scoped keys when needed.

Risk: A persistent global CLI install leaves an executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent execution path is preferred.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference hosted media URLs returned by dLazy services.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
