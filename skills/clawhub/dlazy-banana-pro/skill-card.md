## Description:

Generate and edit images with Nano Banana Pro from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI requires a dLazy account and API key.

Mitigation: Review the pinned CLI before installing and manage the API key in your dLazy account.

Risk: Local images supplied to the CLI are uploaded to dLazy; generated images may be saved locally.

Mitigation: Provide only images intended for upload and approve the destination before using --save.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image links, Image files, Shell commands]

**Output Format:** [Image URLs or saved image files, with JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets may be downloaded to a user-approved path.]

## Skill Version(s):

1.2.31 (source: ClawHub release metadata; skill frontmatter lists 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
