## Description:

Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator model attribution, and return confidence scores for thresholding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check images, videos, or audio for AI-generation signals, deepfake indicators, and likely generator attribution through the dLazy hosted detection service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media may be uploaded to dLazy media storage and analyzed by dLazy's hosted service.

Mitigation: Confirm the exact file path or public URL before invoking detection, especially for private, biometric, confidential, or customer media.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use only trusted environments, protect the local configuration file, or provide the key per invocation with DLAZY_API_KEY when persistence is not desired.

Risk: Detection calls can fail because of missing credentials, insufficient balance, unreachable private URLs, or provider rate limits.

Mitigation: Check authentication and account balance before use, pass only publicly reachable URLs for remote media, and surface returned error codes clearly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON detection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection results may include AI-generation confidence, deepfake confidence, likely generator attribution, audio AI score, frame count, and asynchronous task status.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
