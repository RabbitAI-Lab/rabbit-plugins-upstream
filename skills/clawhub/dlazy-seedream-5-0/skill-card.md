## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy hosted Seedream 5.0 image-generation service from an agent workflow, using text prompts and optional reference images to produce high-resolution image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the dLazy hosted API, and generated outputs are hosted by dLazy.

Mitigation: Avoid sending private images or sensitive prompt content unless that matches the intended use and data handling requirements.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use the documented login or auth flow, keep local configuration access restricted, and rotate or revoke organization API keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON containing generated image output URLs, with an optional downloaded image file when a save path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous mode can return a task identifier for later polling.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
