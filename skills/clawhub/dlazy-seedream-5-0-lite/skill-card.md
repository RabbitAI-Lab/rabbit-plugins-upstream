## Description:

Generates images with Doubao Seedream 5.0 Lite from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts or transform reference images through the dLazy Seedream service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags a login command that may not match the image-generation purpose; the CLI package and referenced local paths were not resolved.

Mitigation: Review the pinned CLI package and confirm the login step is expected before installing or using it.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image files and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before image URLs are available.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
