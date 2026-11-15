## Description:

Generates images with Doubao Seedream 4.5 from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to generate images with Doubao Seedream 4.5 from text prompts, optionally guided by reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a capability mismatch: it observed a CLI login command rather than image generation, and the review was partial because some local references could not be resolved.

Mitigation: Before relying on image generation, verify the installed CLI's Seedream command and review the unresolved references; the available scan evidence does not establish their contents.

## Reference(s):

- [dLazy CLI source repository (declared by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with generated image URLs, optionally saved as image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image with up to 10 reference images; 2K or 4K resolution.]

## Skill Version(s):

1.3.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
