## Description:

Generates 4MP raster images suitable for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate high-resolution images from text prompts through dLazy's hosted Recraft V4 Pro service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI executes third-party code.

Mitigation: Review the pinned @dlazy/cli package before installing.

Risk: Prompts and supplied local media may be sent to dLazy's hosted service.

Mitigation: Only provide prompts and files you are comfortable sharing with the service.

Risk: The saved API key is a reusable credential.

Mitigation: Protect the credential and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image URLs]

**Output Format:** [CLI command and JSON response with hosted image URL; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation can be asynchronous; the CLI can save the resulting image locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release; skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
