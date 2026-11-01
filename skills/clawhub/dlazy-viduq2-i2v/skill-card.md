## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use an agent to turn reference images or first and last frames into short videos, with prompts and options for duration, aspect ratio, resolution, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and local media files are uploaded for generation.

Mitigation: Use only media you are comfortable uploading to dLazy and review the service terms.

Risk: Video generation consumes service credits, and the CLI stores the service key in a local configuration file.

Mitigation: Check estimated costs before generation and keep the local configuration file accessible only to your account; rotate or revoke the key if needed.

Risk: The security inspection covers the skill instructions, not the full external CLI package.

Mitigation: Review the pinned CLI package and its source before installing it.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Guidance]

**Output Format:** [Hosted video URL or saved video file, with JSON status for asynchronous jobs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video duration, aspect ratio, resolution, and optional audio are configurable.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
