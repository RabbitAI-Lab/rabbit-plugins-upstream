## Description:

Selects a dLazy image model to generate or edit images from prompts and optional reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy image-generation, editing, upscaling, or vectorization commands for visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Confirm the service is acceptable for the data before uploading sensitive content.

Risk: Running a third-party CLI requires an API key.

Mitigation: Review the CLI before installation and protect or rotate the API key as needed.

Risk: Generation may spend account credits.

Mitigation: Check account balance and expected usage before running paid requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source linked in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and CLI commands; generated image URLs returned by the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return URLs for generated or edited raster images and SVG assets.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
