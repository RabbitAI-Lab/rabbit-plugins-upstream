## Description:

Detects signs of AI generation in images, videos, and audio, including visual deepfakes and likely generator models, with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can check images, videos, or audio for signs of AI generation and review confidence scores, potential deepfakes, and likely generator models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio submitted for detection are uploaded to dLazy infrastructure.

Mitigation: Submit private, biometric, confidential, or regulated media only when third-party processing is acceptable.

Risk: Authentication saves a dLazy API key locally.

Mitigation: Protect access to the local credentials and avoid sharing the saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [JSON with a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes AI-generation and deepfake confidence scores and a likely generator when available.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
