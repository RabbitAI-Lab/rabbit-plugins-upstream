## Description:

Generates 4MP raster images from text prompts for print-ready and large-format creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request high-resolution raster images for print and large-format projects through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI executes software outside the skill files.

Mitigation: Review the package and its source before installing the pinned CLI.

Risk: Prompts, parameters, and files explicitly supplied to the CLI are sent to dLazy's hosted service.

Mitigation: Share only content you are comfortable sending to dLazy.

Risk: A locally stored dLazy API key can be exposed on an untrusted machine.

Mitigation: Store it only on trusted devices and rotate or revoke it in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing image URLs; an optional save command downloads the image.]

## Skill Version(s):

1.3.32 (source: ClawHub release; bundled skill frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
