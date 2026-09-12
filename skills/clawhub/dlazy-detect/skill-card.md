## Description:

Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator attribution, and return confidence scores for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content-review workflows use this skill to ask an agent to run dLazy media detection for images, videos, or audio. It helps review whether media appears AI-generated, contains a deepfake, or matches a likely generator model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media may be uploaded to dLazy media storage and sent to the hosted dLazy detection service.

Mitigation: Use the skill only with media approved for third-party processing, and avoid private or sensitive files unless that sharing is acceptable.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, use per-user credentials, and rotate the key if it is exposed.

Risk: Broad detect-related triggers could invoke the hosted service when the user intended a different kind of detection.

Mitigation: Confirm that the request is specifically for AI media detection before running the command.

Risk: Detection verdicts are confidence-based and may be sensitive to thresholds or media quality.

Mitigation: Treat results as decision support and review raw confidence scores before taking consequential action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Text and JSON detection results with optional shell commands for authentication and execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include confidence scores, boolean verdict fields, likely generator attribution when available, and asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
