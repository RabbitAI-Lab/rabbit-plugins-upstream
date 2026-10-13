## Description:

Generates Vidu Q2 images from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request images from text prompts or reference images using Vidu Q2 through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication stores a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Prompts and selected local reference images are sent to the dLazy cloud service.

Mitigation: Confirm the content is appropriate to share before submitting prompts or uploading images.

Risk: Image-generation requests may consume dLazy credits.

Mitigation: Confirm paid requests with the user and check the cost estimate before execution.

Risk: Installing the third-party CLI adds executable software to the environment.

Mitigation: Review the pinned package before use; choose the on-demand npx option if a persistent installation is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI homepage (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text with shell commands and JSON image-result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful requests return image URLs; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
