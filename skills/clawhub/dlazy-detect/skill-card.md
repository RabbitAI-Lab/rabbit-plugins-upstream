## Description:

Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator attribution, and return confidence scores for decision thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content review agents use this skill to check images, videos, or audio for AI generation, deepfake indicators, and likely generator attribution. It is intended for media analysis workflows that need structured confidence scores and a short human-readable verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio may be uploaded to dLazy infrastructure for detection.

Mitigation: Do not analyze private, sensitive, biometric, or confidential media unless uploading it to dLazy infrastructure is acceptable.

Risk: The skill requires dLazy API authentication and may store credentials in local CLI configuration.

Mitigation: On shared systems, pass DLAZY_API_KEY per invocation instead of saving an API key in the local config.

Risk: Detection depends on a hosted external service and may fail because of missing credentials, insufficient balance, or provider rate limits.

Mitigation: Check authentication, credits, and rate-limit status before relying on the skill in automated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON results with a human-readable text summary and optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns AI-generated, deepfake, audio-generation, and likely-generator confidence scores when detection completes; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.0.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
