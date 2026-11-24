## Description:

Generates high-resolution, 4-megapixel raster images suitable for print-ready and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to create high-resolution raster images from prompts, with optional aspect-ratio control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence and partial coverage; it notes that the relationship between required login/API-key setup and image generation is not fully established in the reviewed materials.

Mitigation: Review the full instructions and CLI package before installation, and configure credentials only for an account you control.

Risk: The skill sends prompts to dLazy's hosted API and uploads supplied local media files to its media storage.

Mitigation: Avoid submitting sensitive prompts or files unless you are comfortable sharing them with the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (linked in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Raster image (PNG) with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image is returned by URL and can be saved to a local path; asynchronous runs may return a task identifier.]

## Skill Version(s):

1.3.43 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
