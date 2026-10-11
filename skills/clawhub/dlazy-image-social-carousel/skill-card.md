## Description:

Guides agents through visual direction, slide planning, and cover-first generation of social-media carousels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate coordinated social-media carousel slides, approving the visual direction and cover before continuing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external CLI exposes the environment to third-party code.

Mitigation: Review the @dlazy/cli package before use and prefer npx if a global installation is not desired.

Risk: An API key is stored locally, and prompts or user-provided media may be sent to dLazy's hosted service.

Mitigation: Use a scoped, rotatable key and provide private media only when its upload is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown planning tables, generation guidance, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cover-first workflow with user approval before subsequent slides]

## Skill Version(s):

1.3.28 (source: ClawHub release; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
