## Description:

Generate images with the Kling o1 model from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate images from text prompts or edit and create images using reference images with Kling o1.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media are sent to dLazy's hosted service; local reference files are uploaded and generated assets are hosted there.

Mitigation: Submit only media you intend to share with dLazy, prefer device login over sharing an API key in chat, and check generation costs.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image files, JSON result and task metadata]

**Output Format:** [Image URLs or saved image files with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be saved to a local path; asynchronous requests may return a task identifier before the image is ready.]

## Skill Version(s):

1.3.36 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
