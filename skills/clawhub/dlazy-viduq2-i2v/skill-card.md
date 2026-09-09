## Description:

图生视频 Vidu Q2 converts static images into dynamic videos using the dLazy-hosted Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external agents use this skill to invoke dLazy's Vidu Q2 image-to-video CLI for generating videos from reference images, prompts, frame controls, aspect ratio, resolution, and optional async or save behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use of a third-party hosted service sends prompts and generation parameters to dLazy's API.

Mitigation: Install and run the skill only if dLazy's hosted service is acceptable for the intended data and use case.

Risk: Local image, video, or audio paths supplied to media fields may be uploaded to dLazy media storage for model processing.

Mitigation: Confirm before uploading private or sensitive media, and avoid submitting content that should not leave the local environment.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use least-privileged credential handling, avoid exposing the key in logs or shell history, and rotate or revoke it when no longer needed.

Risk: The skill can be installed as a global npm package, which persists a CLI on the system.

Mitigation: Prefer npx or another least-privileged install path when possible, and avoid sudo for installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API-key setup, dry runs, asynchronous polling, and saving generated media URLs or files.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
