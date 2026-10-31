## Description:

Generates and edits images with GPT Image 2.5 Flare through the dLazy service, with reference image, aspect ratio, and quality options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image creators can use an agent to generate images from prompts or edit images using reference inputs, then receive or save the resulting image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the third-party dLazy service, and local input files may be uploaded for processing.

Mitigation: Share only prompts and images that are appropriate to send to that service.

Risk: Image generation uses paid dLazy credits.

Mitigation: Review the cost estimate and available credits before high-volume generation.

Risk: The workflow requires a dLazy API key, and the documented install uses a pinned CLI package.

Mitigation: Protect the API key and review the pinned CLI package before installation; rotate or revoke the key if needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link from skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image assets with a JSON result containing hosted URLs; optionally saved to a local path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images, aspect ratio and quality settings; asynchronous requests can return a task identifier.]

## Skill Version(s):

1.2.25 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
