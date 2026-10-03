## Description:

Generates 4MP raster images from text prompts for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request high-resolution raster images for print-ready designs and large-format projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media files explicitly provided for generation may be sent to dLazy's cloud service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: Logging in may save an API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run credentials if persistent storage is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a hosted image URL or saved image path.]

## Skill Version(s):

1.3.24 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
