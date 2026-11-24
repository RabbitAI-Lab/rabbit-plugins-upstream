## Description:

Image super-resolution tool: enhances image clarity and details, returning enhanced URL, suitable for low-res asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can upscale low-resolution images to improve visible clarity and detail, then use the returned image URL or save the enhanced asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports an unexplained login operation unrelated to image upscaling; the review was partial and confidence is medium.

Mitigation: Before connecting an account, review the CLI login flow and requested access against the publisher's documentation.

Risk: The skill sends request parameters and local image files to dLazy-hosted services.

Mitigation: Submit only images and content you are authorized to upload, and review the service's data handling terms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source (skill-declared link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Enhanced image asset, Image URL, JSON result]

**Output Format:** [JSON response containing an enhanced image URL; optionally saves the image as a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An asynchronous request can return a task ID before the image is ready.]

## Skill Version(s):

1.3.44 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
