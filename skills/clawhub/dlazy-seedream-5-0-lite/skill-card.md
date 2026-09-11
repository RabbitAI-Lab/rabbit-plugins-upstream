## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts or transform supplied reference images through the dLazy hosted Seedream 5.0 Lite CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external CLI and hosted API that require authentication.

Mitigation: Review the dLazy CLI source or npm package before installation in sensitive environments, avoid elevated npm/npx execution, and use scoped or per-invocation credentials where practical.

Risk: Prompts and selected local image paths are sent to dLazy services for generation.

Mitigation: Only provide prompts and media files that are appropriate to upload to dLazy, and rotate or revoke stored API keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI commands with JSON responses containing image asset URLs or async task identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as hosted URLs and can be saved locally with the CLI.]

## Skill Version(s):

1.3.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
