## Description:

GPT Image 2 model for text-to-image and image editing, including edits and synthesis with reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use this skill to generate images from text prompts or edit and synthesize images using reference images through dLazy's hosted GPT Image 2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's hosted service, and local image files may be uploaded for processing.

Mitigation: Upload only images you intend to share and review the service terms before sending sensitive content.

Risk: The CLI stores an API key in local configuration, and requests spend service credits.

Mitigation: Protect the local configuration, rotate or revoke exposed keys, and check credit costs before making requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JPEG, PNG, or WebP image files with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a text prompt and optionally up to five reference images; size and quality are configurable, and asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
