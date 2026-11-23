## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts or create variations from reference images with Vidu Q2 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security scan noted a mismatch between the image-generation description and a `dlazy login` command; its benign verdict is not a safety guarantee.

Mitigation: Review the command and CLI source before running it, and provide API credentials only to a CLI you trust.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Image assets returned as URLs or saved files, with JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image; asynchronous requests may return a task identifier before image outputs are ready.]

## Skill Version(s):

1.3.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
