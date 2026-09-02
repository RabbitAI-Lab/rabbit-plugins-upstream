## Description:

Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator attribution, and return confidence scores for decision thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content reviewers use this skill to check image, video, or audio files for AI generation, deepfake indicators, and likely generator attribution. It is not intended for text detection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio may be uploaded to dLazy media storage and analyzed by a third-party detection backend.

Mitigation: Use the skill only for explicit media-detection requests, avoid private or regulated media unless consent and policy allow it, and prefer public URLs only when they are intended to be accessible.

Risk: API keys may be saved in the local dLazy CLI configuration.

Mitigation: Prefer per-run API keys for sensitive environments or review local config handling before storing credentials.

Risk: Broad trigger phrases could cause the skill to be considered for unrelated detection tasks.

Mitigation: Invoke it only for image, video, or audio AI-detection requests and do not use it for text detection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON results with a human-readable text summary and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns AI-generated, deepfake, audio-generation, and likely-generator confidence scores; asynchronous runs may return a task identifier for later polling.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
