## Description:

Generate and edit high-quality images with Nano Banana 2.0 using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to generate images from prompts or edit images using supplied reference images. The skill guides use of the dLazy image-generation service through its CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied assessment has medium confidence and partial coverage; it notes the advertised image features were not demonstrated and the CLI package and some referenced paths were not assessed.

Mitigation: Review the skill's purpose and the pinned CLI package before installing it or providing login credentials.

Risk: Prompts and local reference-image files are sent to dLazy-hosted services when used, according to the skill documentation.

Mitigation: Avoid sending sensitive prompts or images unless you are comfortable with the service receiving them.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON, Guidance]

**Output Format:** [JSON result with generated image URLs or asynchronous task status]

**Output Parameters:** [Text prompt with optional reference images and generation settings]

**Other Properties Related to Output:** [Generated assets are hosted by the dLazy media service.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
