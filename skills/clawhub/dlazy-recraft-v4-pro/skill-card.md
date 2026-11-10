## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-scale use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate high-resolution raster artwork with Recraft V4 Pro through dLazy. It is suited to print-ready assets and large-format imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence but partial; it flags authentication steps that do not clearly match the image-generation purpose and notes unresolved local references.

Mitigation: Review the CLI authentication flow and linked package materials before configuring an API key.

Risk: Prompts and any supplied local media are sent to dLazy hosted services for generation.

Mitigation: Avoid submitting sensitive prompts or files unless they are approved for processing by that service.

## Reference(s):

- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON response with generated image URLs; optionally a downloaded raster image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [High-resolution raster output; the skill describes 4MP images and supports optional local saving.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
