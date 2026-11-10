## Description:

Convert static images into dynamic videos with the Vidu Q2 image-to-video model, using prompts and generation settings to guide the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn reference images into short videos with prompts, optional first and last frames, and controls for duration, aspect ratio, resolution, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login flow stores a dLazy API key locally, and prompts or supplied media are sent to dLazy-hosted services.

Mitigation: Review the account access and service terms before signing in or sending sensitive material; rotate or revoke the API key when needed.

Risk: The security review did not inspect the CLI or resolve several references, and the login command's connection to image-to-video generation is unclear.

Mitigation: Review the pinned CLI package and its documented login flow before installation, and start with non-sensitive inputs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI project link listed in skill metadata (GitHub provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, Hosted media URLs, JSON task and result metadata]

**Output Format:** [Generated video asset, returned as a hosted URL or saved file, with JSON task/result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and configurable generation settings.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
