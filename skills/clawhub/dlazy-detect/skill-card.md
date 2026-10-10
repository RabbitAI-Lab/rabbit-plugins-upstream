## Description:

Detects AI-generated images, videos, and audio, including visual deepfakes, and returns confidence scores and likely generator attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and developers use this skill to check images, video, and audio for signs of AI generation or deepfakes and review confidence scores before making a decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files are uploaded to dLazy for analysis; submitted URLs and media may contain private, biometric, confidential, or regulated information.

Mitigation: Submit media only when authorized and comfortable sharing it with dLazy; avoid sensitive material unless its handling is approved.

Risk: The CLI may save an API key locally, and analysis requests may consume API quota or credits.

Mitigation: Use a per-invocation DLAZY_API_KEY when local key storage is unwanted, and check quota or credits before submitting media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text summary and structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence scores, deepfake assessment, and likely generator; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.0.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
