## Description:

Generates stylized images from prompts with configurable aspect ratio, bot type, and grid or U1–U4 output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized images through dLazy using a text prompt and optional aspect ratio, bot type, and image selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI sends prompts and any explicitly provided media files to dLazy's hosted service.

Mitigation: Review the CLI package before installing; only submit prompts and local files you intend to share.

Risk: Logging in saves a persistent API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if you do not want a saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Text, Files]

**Output Format:** [JSON response with generated image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grid or U1–U4 selection; asynchronous requests can return a task ID instead of an image.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
