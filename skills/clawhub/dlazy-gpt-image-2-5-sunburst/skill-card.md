## Description:

GPT Image 2.5 Sunburst supports text-to-image generation and image editing, with reference images, aspect ratios up to 21:9, and quality settings up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use this skill to generate images from prompts or edit images using reference inputs, with controls for aspect ratio and output quality. Prompts and supplied local images are sent to dLazy's hosted service for processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a benign verdict with medium confidence and an incomplete scan because Skillspector could not resolve the CLI package reference.

Mitigation: Before installing, check that the pinned @dlazy/cli package and its authentication flow match your expectations.

Risk: Prompts and any supplied local reference images are uploaded to dLazy's hosted service for processing.

Mitigation: Only submit prompts and images that are appropriate to send to the service, and protect or revoke the associated API key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [PNG image files with a JSON result envelope containing output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference images, aspect ratio, and quality settings; asynchronous requests can return a task ID before the image is ready.]

## Skill Version(s):

1.2.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
