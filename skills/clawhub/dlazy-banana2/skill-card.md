## Description:

Generate and edit high-quality images with Nano Banana 2.0 using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to request dLazy Nano Banana 2 image generation or editing from an agent, including text-to-image and image-to-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted image service.

Mitigation: Use only prompts and media that are appropriate to share with dLazy, and avoid local image paths unless uploading those files is intended.

Risk: The skill depends on a third-party CLI for execution.

Mitigation: Prefer the pinned npx invocation or review the linked CLI source before choosing a global installation.

Risk: The service requires a dLazy API key.

Mitigation: Use a revocable API key and rotate or revoke it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response containing generated image URLs, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests can return a generateId for polling; saved outputs are downloaded only when a save path is provided.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
