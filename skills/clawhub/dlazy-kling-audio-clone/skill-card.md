## Description:

Generate customized speech that highly restores the timbre by uploading reference audio using Kling Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create cloned custom speech through the dLazy CLI by submitting reference audio to the hosted Kling Audio Clone service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice-related content is uploaded to dLazy services for processing.

Mitigation: Only upload audio that the user has permission to clone, and avoid sensitive voice samples unless the user accepts the service exposure.

Risk: API keys may be saved in the local dLazy CLI configuration.

Mitigation: Use the per-run DLAZY_API_KEY environment variable instead of saved credentials on shared machines or when local credential persistence is a concern.

Risk: The security verdict is suspicious because file-permission guarantees for saved credentials are weaker than claimed.

Mitigation: Review the skill and local credential storage behavior before installing or using it in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-audio-clone)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or an asynchronous task identifier for polling.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
