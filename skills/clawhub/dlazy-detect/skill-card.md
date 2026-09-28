## Description:

Checks images, videos, and audio for signs of AI generation, including visual deepfakes and likely generator models, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing images, videos, or audio use this skill to assess whether media may be AI-generated and to review deepfake or generator-model confidence scores when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images, videos, or audio may be uploaded to dLazy's hosted service without an explicit confirmation step.

Mitigation: Confirm the intended upload and review dLazy's data handling terms before using private, regulated, or confidential media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON results with a plain-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence scores; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
