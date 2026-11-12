## Description:

Detects whether image, video, or audio files are AI-generated, including visual deepfakes and likely generator models, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content reviewers use the skill to assess whether images, videos, or audio are AI-generated, detect face swaps, and inspect likely generator attribution through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review did not establish the CLI login credential handling or destination.

Mitigation: Review the authentication setup and confirm the credential destination before signing in.

Risk: Local media files are uploaded to dLazy media storage for analysis.

Mitigation: Submit only media you are authorized to share and check applicable privacy requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON results with a human-readable text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence scores, boolean verdicts, and likely generator attribution for supported media; text input is unsupported.]

## Skill Version(s):

1.0.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
