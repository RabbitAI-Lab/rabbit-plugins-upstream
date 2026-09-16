## Description:

Generate images with the Kling o1 model from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy CLI for Kling o1 text-to-image and image-to-image generation, including optional asynchronous generation and saving returned image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media are sent to a third-party cloud service for generation.

Mitigation: Avoid sending sensitive prompts or images unless the user accepts dLazy's handling of that data.

Risk: The skill relies on a dLazy API key stored locally or provided through an environment variable.

Mitigation: Use a revocable organization-scoped API key and rotate or revoke it when access is no longer needed.

Risk: Generated requests may consume dLazy credits.

Mitigation: Use dry-run or review command parameters before making generation calls when cost control matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional downloaded image files, and concise markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; generated images and uploaded reference media are handled through dLazy cloud endpoints.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
