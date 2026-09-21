## Description:

Generate/edit images with Nano Banana Pro, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy Nano Banana Pro hosted API from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media are sent to dLazy-hosted endpoints for generation.

Mitigation: Confirm the user is comfortable sending the prompt and media to dLazy before invoking the CLI, especially for confidential or regulated content.

Risk: The skill depends on a third-party CLI package and hosted service.

Mitigation: Use the pinned @dlazy/cli 1.2.3 package and review the package/source before installing or running it.

Risk: The workflow requires a dLazy API key stored locally or supplied through an environment variable.

Mitigation: Use a key that can be rotated or revoked, and avoid exposing it in prompts, logs, or shared command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples; CLI responses include image output URLs and can save image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package, requires npm or npx, and requires a dLazy API key.]

## Skill Version(s):

1.2.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
