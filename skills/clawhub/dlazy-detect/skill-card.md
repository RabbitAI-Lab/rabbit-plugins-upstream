## Description:

Detects whether image, video, or audio media is AI-generated, including visual deepfakes and likely generator model, and returns thresholdable confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to check image, video, or audio media for AI generation, visual deepfakes, and likely generator attribution. It is suited for media review workflows that need confidence scores and a short human-readable verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media files or public media URLs may be sent to dLazy and Hive-backed remote services for analysis.

Mitigation: Use the skill only for media whose handling is compatible with dLazy retention, privacy, and compliance terms; avoid highly sensitive, regulated, or private biometric media unless those terms meet the user's requirements.

Risk: The skill requires a dLazy API key and may store that key in local CLI configuration.

Mitigation: Protect the local configuration file and prefer per-invocation environment variables when a persistent local credential is not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Text, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples; runtime CLI responses include JSON outputs and a short text verdict.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts exactly one image, video, or audio input per detection command; asynchronous runs may require polling by task ID.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
