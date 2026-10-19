## Description:

Selects a dLazy image model to generate or edit images from a user's prompt and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select an image model and generate, edit, upscale, or vectorize visual assets through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy's cloud service, and generated images are hosted there.

Mitigation: Avoid sensitive prompts and files unless sharing them with dLazy is acceptable.

Risk: Authentication may store an API key locally; a global CLI install persists on the device.

Mitigation: Protect or rotate the API key as needed, and use the pinned npx invocation if a persistent CLI install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results may link to files hosted by dLazy.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
