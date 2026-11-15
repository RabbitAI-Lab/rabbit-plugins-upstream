## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can create images from text prompts or edit images using up to ten reference images, with Vidu Q2 options for aspect ratio and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial: six local references were unresolved, including CLI-related references, and the external CLI’s internal behavior was not shown. The reported login command has no demonstrated connection to image generation.

Mitigation: Review the install and login details and the CLI source before installing, and confirm the login behavior is expected for this image-generation task.

Risk: Prompts and any local reference images are sent to dLazy’s hosted API and media storage for processing.

Mitigation: Do not submit sensitive prompts or images unless they are approved for processing by the dLazy service.

## Reference(s):

- [dLazy CLI source linked by the skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, API Calls, Shell commands]

**Output Format:** [Generated image assets (PNG) returned through hosted URLs, with a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier before image outputs are ready.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
