## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn Chinese or English text into speech, choose a supported voice and speaking speed, and save the generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for generation is processed by dLazy and may contain sensitive information.

Mitigation: Avoid submitting confidential text unless the service privacy terms have been reviewed.

Risk: Speech generation can incur charges, and the saved API key grants access to the dLazy organization.

Mitigation: Check generation costs, protect the local CLI configuration, and rotate or revoke the key when needed.

Risk: Installing the pinned CLI adds an executable dependency.

Mitigation: Review the pinned CLI package and project before installation.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Shell commands, Configuration instructions]

**Output Format:** [Generated speech audio and CLI result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Chinese and English voices, adjustable speaking speed, and an optional save path; generation requires a dLazy API key and may incur charges.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
