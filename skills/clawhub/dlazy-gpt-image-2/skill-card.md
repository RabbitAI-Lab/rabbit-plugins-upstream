## Description:

GPT Image 2 model for generating images from text and editing or synthesizing images with reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to generate images from text prompts or edit and synthesize images with reference inputs through dLazy's hosted GPT Image 2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence and partial analysis; it notes a login command that may not fit the image-generation purpose.

Mitigation: Review the CLI's stated behavior and consider whether its login flow is appropriate before authenticating.

Risk: Prompts are sent to dLazy for inference, and local reference images are uploaded to its media service.

Mitigation: Review the service terms and avoid submitting sensitive prompts or images unless you are comfortable sharing them with the hosted service.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated image URLs in a JSON response; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a text prompt and optional reference images; local reference files are uploaded to dLazy's media service.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
