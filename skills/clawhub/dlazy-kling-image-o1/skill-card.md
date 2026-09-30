## Description:

Guides agents to generate or edit images with Kling Image O1 using text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through text-to-image generation or image editing with reference images using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication may store a dLazy API key on the local device.

Mitigation: Trust the CLI before installation; use a per-invocation key when local persistence is undesirable and rotate or revoke exposed keys.

Risk: Prompts and selected reference images are sent to dLazy, and generated images are hosted on its infrastructure.

Mitigation: Share only content approved for the service and review hosted output links before distributing them.

Risk: Image-generation requests may incur charges.

Mitigation: Check the estimated cost with the CLI's dry-run option before submitting a request.

## Reference(s):

- [dLazy CLI (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and shell commands; the CLI returns JSON containing image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted by dLazy; users can optionally save them locally.]

## Skill Version(s):

1.3.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
