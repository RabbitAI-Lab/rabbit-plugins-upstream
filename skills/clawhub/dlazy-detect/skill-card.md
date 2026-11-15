## Description:

Detect whether images, videos, or audio are AI-generated, identify possible deepfakes and likely generators, and return confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can submit an image, video, or audio file or public URL to receive AI-generation and deepfake confidence scores and a likely generator attribution. The skill requires a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security guidance reports a partial, medium-confidence scan and an unresolved mismatch between the stated media-detection purpose and observed login behavior.

Mitigation: Review the flagged gaps and clarify the behavior before relying on the skill's detection results.

Risk: Local media files are uploaded to dLazy hosted media storage for processing.

Mitigation: Submit only media you are permitted to share with dLazy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON verdict with a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence scores, boolean verdicts, likely generator attribution, and optional asynchronous task status.]

## Skill Version(s):

1.0.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
