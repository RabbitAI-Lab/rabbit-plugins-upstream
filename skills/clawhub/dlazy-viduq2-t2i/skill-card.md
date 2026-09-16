## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to invoke the dLazy Vidu Q2 CLI for generating image assets from prompts or prompt-plus-image inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy CLI package and hosted service, and prompts or selected local media may be uploaded to dLazy endpoints.

Mitigation: Install only if comfortable trusting the dLazy CLI and service, and pass only prompts or local media files intended for upload.

Risk: The dLazy CLI uses local credential configuration for API access.

Mitigation: Prefer npx or a non-privileged local install, protect the local config, and rotate or revoke the API key if access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image files, Shell commands, Guidance]

**Output Format:** [JSON CLI response containing generated image URLs, with optional downloaded image files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs when --no-wait is used.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
