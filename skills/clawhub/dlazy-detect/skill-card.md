## Description:

Detects whether image, video, or audio media is AI-generated, including visual deepfakes and likely generator attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to check media for likely AI generation, visual deepfakes, and generator attribution from a command-line workflow. It is intended for image, video, and audio inputs, not text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image, video, or audio files can be uploaded to dLazy's hosted service for analysis.

Mitigation: Use the skill only with media you are comfortable sending to that service, prefer public URLs when appropriate, and avoid sensitive local files unless upload is intended.

Risk: The CLI requires a dLazy API key and stores it in the user's local configuration unless supplied per invocation.

Mitigation: Use normal user-level installation and configuration, protect the API key, and avoid installing or running the package with elevated privileges.

Risk: The detector does not support text inputs and returns confidence scores that require thresholding.

Mitigation: Use it only for image, video, or audio media and review confidence scores before making consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON result objects with a human-readable text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exactly one image, video, or audio input; local media may be uploaded to dLazy media storage for analysis.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
