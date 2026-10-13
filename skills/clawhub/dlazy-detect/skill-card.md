## Description:

Checks images, videos, and audio for signs of AI generation, including visual deepfakes and likely generator models, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content reviewers use this skill to check images, videos, or audio for AI-generated content and visual deepfakes, using confidence scores to guide further review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio submitted for detection are uploaded to dLazy for remote analysis.

Mitigation: Avoid submitting confidential or highly sensitive media unless the upload is acceptable.

Risk: Logging in or saving an API key can persist credentials in the local CLI configuration.

Mitigation: Use a per-invocation API key when you do not want credentials stored locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured JSON detection results with a human-readable text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes AI-generation and deepfake confidence scores, likely generator details when available, and threshold-based verdicts; text input is not supported.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
