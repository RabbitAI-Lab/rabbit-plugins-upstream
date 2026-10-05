## Description:

Guides agents in generating and editing images with Nano Banana Pro using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to create images from text prompts or edit images using reference images through dLazy's hosted Nano Banana Pro service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be uploaded to dLazy's hosted service.

Mitigation: Send only content you intend to share with dLazy and review media before submission.

Risk: Authentication stores an API key locally unless supplied per invocation.

Mitigation: Protect the local CLI configuration or use the per-invocation environment variable.

Risk: Installing the pinned third-party npm CLI introduces a software supply-chain dependency.

Mitigation: Review the pinned CLI package before installing in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted image URLs and can optionally save generated images locally.]

## Skill Version(s):

1.2.28 (source: ClawHub release; bundled skill frontmatter states 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
