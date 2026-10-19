## Description:

Helps agents generate and edit images with Nano Banana Pro using text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in creating images from text prompts or editing images using references through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Share only content approved for external processing, and check media paths before submitting them.

Risk: The dLazy API key is stored in local CLI configuration after login.

Mitigation: Protect the configuration and rotate or revoke the key if it may have been exposed.

Risk: A generic image-generation request could be routed to this third-party provider unexpectedly.

Mitigation: Confirm the user intends to use dLazy before sending prompts or files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be linked or saved locally; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.2.34 (source: ClawHub release metadata; supplied skill files state 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
