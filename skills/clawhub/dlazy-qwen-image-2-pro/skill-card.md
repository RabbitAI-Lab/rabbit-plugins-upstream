## Description:

Generates images with Qwen Image 2 Pro from text prompts, with optional reference images and controls for size and prompt rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts, optionally supplying reference images for image-guided results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: Login can save an API key in the user's local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if persistent key storage is undesirable.

Risk: Using the skill requires installing an external CLI package.

Mitigation: Review the @dlazy/cli package before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with generated image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before images are ready.]

## Skill Version(s):

1.3.30 (source: ClawHub release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
