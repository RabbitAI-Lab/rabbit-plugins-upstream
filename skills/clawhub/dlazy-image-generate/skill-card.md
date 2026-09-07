## Description:

Image generation skill that selects an appropriate dLazy CLI image model from a user prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to select and run dLazy CLI models for text-to-image generation, image editing, matting, vectorization, and upscaling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent to dLazy cloud services.

Mitigation: Only pass files and prompts that are appropriate to upload to dLazy, and review service terms before use.

Risk: The dLazy API key is a credential that can authorize usage and billing.

Mitigation: Store it using the documented login or auth flow, avoid exposing it in logs or prompts, and rotate it if exposed.

Risk: Installing a third-party CLI globally can increase local environment exposure.

Mitigation: Review the dLazy CLI source or package before installing, and use the pinned npx invocation when a persistent global binary is not needed.

Risk: Generation requests may consume dLazy credits.

Mitigation: Confirm account balance and intended cost before large or repeated generations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI commands return JSON envelopes with generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
