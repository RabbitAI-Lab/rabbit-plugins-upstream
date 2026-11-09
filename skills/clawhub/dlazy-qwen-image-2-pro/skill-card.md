## Description:

Generates images with Alibaba Bailian's Qwen Image 2 Pro model, including detailed scenes and text-rich layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to generate images from text prompts, optionally with reference images, and receive an image URL or save the result as a file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial: it could not verify referenced package and implementation details, and noted that the observed login command does not clearly match the image-generation purpose.

Mitigation: Review the linked CLI package and dLazy service authentication details before installing or signing in.

Risk: Prompts and supplied local media are sent to dLazy-hosted services, and generated assets are hosted there.

Mitigation: Avoid sending sensitive prompts or files unless the service is approved for that data, and review its service terms.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets as hosted URLs or saved files, with a JSON result envelope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests return a task ID until generation completes.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
