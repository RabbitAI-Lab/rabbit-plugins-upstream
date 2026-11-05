## Description:

GPT Image 2 generates images from text prompts and edits or synthesizes images using reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate images from text prompts or edit and synthesize images with reference images through dLazy's GPT Image 2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy; local image paths are uploaded for processing.

Mitigation: Send only material you are permitted to share with the service, and review dLazy's terms before use.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, avoid exposing the key, and rotate or revoke it from the organization dashboard if needed.

Risk: The external CLI executable, hosted service, and claimed credential-file protections were not fully audited.

Mitigation: Review the listed CLI project and service terms before use, and apply your organization's credential-handling requirements.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JPEG, PNG, or WebP image assets with a JSON result envelope]

**Output Parameters:** [1D (text prompt; optional reference images)]

**Other Properties Related to Output:** [Up to five reference images; size and quality are selectable. Results may be saved locally, and asynchronous requests can return a task ID before an image is ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
