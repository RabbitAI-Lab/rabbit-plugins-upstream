## Description:

Uses dLazy's hosted GPT Image 2 service to generate images from text prompts and edit or combine images with reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate images from prompts or edit and combine reference images through dLazy's hosted GPT Image 2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and flagged an unexplained login action; some local references could not be resolved.

Mitigation: Review the login workflow and resolve the referenced files before installing.

Risk: Prompts and supplied images are sent to dLazy's hosted service for generation or editing.

Mitigation: Only send prompts and images that are appropriate to share with the hosted service.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [CLI project page](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Generated image assets and CLI JSON results containing image URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be returned as hosted URLs or saved to a local path; asynchronous runs can return a task ID. Prompts and supplied images are sent to dLazy's hosted service.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
