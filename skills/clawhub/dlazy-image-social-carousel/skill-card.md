## Description:

Guides the design of social-media carousels through slide planning, user confirmation, and cover-first image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan platform-specific social-media carousels, approve a visual direction and cover, and generate coordinated slides with dLazy image services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party CLI executes software on the user's device.

Mitigation: Review the dLazy CLI source before choosing a global npm installation or npx execution.

Risk: A dLazy API key is stored locally when signing in through the CLI.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Prompts and referenced media files are sent to dLazy-hosted services.

Mitigation: Obtain permission for supplied media and avoid submitting sensitive content unless the service is approved for it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Design guidance, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with slide plans, approval prompts, command snippets, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests user approval before image generation and checks the cover before continuing with other slides.]

## Skill Version(s):

1.3.24 (source: ClawHub release; supplied skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
