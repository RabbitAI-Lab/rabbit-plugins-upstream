## Description:

Generates stylized Midjourney images with configurable aspect ratios, bot types, and grid or U1–U4 outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request artistic, strongly stylized images through the dLazy CLI, choosing an aspect ratio, Midjourney or Niji Journey bot, and grid or individual upscale output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the advertised image-generation purpose and login or authentication commands; scan confidence is medium and coverage is partial.

Mitigation: Before installing, review the package and unresolved referenced material, and confirm its authentication behavior matches the intended use.

Risk: Prompts and any supplied local media are sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting prompts or media that you are not comfortable sharing with the service.

## Reference(s):

- [Declared dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON response containing image URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and supplied media are sent to dLazy-hosted services.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
