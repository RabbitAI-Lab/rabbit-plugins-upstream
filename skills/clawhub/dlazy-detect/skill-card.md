## Description:

Detects AI-generated images, video, and audio, including visual deepfakes and likely generator models, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams checking images, video, or audio for signs of AI generation can use this skill to obtain confidence scores, deepfake indicators, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media submitted for detection may be uploaded to dLazy-hosted services, and public media URLs are sent for remote analysis.

Mitigation: Submit sensitive, regulated, or private media only when remote processing is intentionally approved.

Risk: Use requires an external npm CLI, a dLazy account, and an API key stored in local CLI configuration.

Mitigation: Review the CLI dependency and local credential storage before installation and authentication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Text summary and structured JSON detection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence scores, AI-generation and deepfake indicators, and likely generator attribution; asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.0.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
