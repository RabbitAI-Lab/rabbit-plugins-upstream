## Description:

Generates 4MP raster images for print-ready assets and large-format uses through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution raster images from text prompts for print and large-format projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly provided media files are sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: The skill requires an external npm CLI package and a locally stored dLazy API key.

Mitigation: Review the package before installation, keep the API key private, and revoke it if compromised; use npx to avoid a persistent global install.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance and CLI JSON response with an image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be downloaded locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
