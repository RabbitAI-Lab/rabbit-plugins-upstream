## Description:

Detect whether images, videos, or audio are AI-generated, flag possible visual deepfakes, and estimate the likely generator model with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to assess whether images, videos, or audio may be AI-generated, identify possible visual deepfakes, and review confidence scores and likely generator attribution. Text is not supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media is sent to dLazy and its analysis provider, and service retention terms are not covered by this review.

Mitigation: Submit only media you are comfortable sharing, and check the service's current media-retention terms.

Risk: The saved API key could be exposed, and detection requests may incur charges.

Mitigation: Protect the saved API key and check service charges before using the skill.

Risk: External CLI behavior and service data handling remain unverified by the security review.

Mitigation: Review the CLI and service terms before processing sensitive media.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-detect)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON results with a human-readable text summary; Markdown usage and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence scores, boolean judgments, and likely generator attribution for image, video, or audio inputs; text inputs are unsupported.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
