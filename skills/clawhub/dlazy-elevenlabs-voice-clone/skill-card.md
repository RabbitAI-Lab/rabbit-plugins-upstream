## Description:

Clones a custom voice from a clean audio sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can submit an authorized clean voice sample to create a custom voice for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The `dlazy login` behavior and referenced CLI package were not fully inspected, leaving some uncertainty in the medium-confidence security assessment.

Mitigation: Review the CLI package and verify what `dlazy login` does and whether it is needed before installing or authenticating.

Risk: The documented workflow uploads local audio samples to dLazy-hosted media storage for processing.

Mitigation: Submit only audio you are authorized to share, and consider the sample's sensitivity before upload.

## Reference(s):

- [CLI source repository (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)

## Skill Output:

**Output Type(s):** [Voice-cloning result, API result data, JSON]

**Output Format:** [JSON response with result or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result may be returned after asynchronous task completion.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
