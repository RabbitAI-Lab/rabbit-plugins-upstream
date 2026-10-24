## Description:

Converts static images into dynamic videos with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn supplied images into videos with Vidu Q2, choosing generation settings such as duration, aspect ratio, and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input media is uploaded to dLazy for cloud generation.

Mitigation: Use only media you are comfortable uploading and review dLazy privacy terms.

Risk: The CLI stores an API key and generation uses service credits.

Mitigation: Protect the stored key and use the documented dry-run option to preview requests and costs.

Risk: The skill depends on an external CLI package.

Mitigation: Review and trust the CLI dependency before installing or running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, API responses, Shell commands]

**Output Format:** [Generated video media and JSON task/result responses; command-line usage is documented in Markdown with shell examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation settings include duration, aspect ratio, resolution, and optional audio; asynchronous jobs may return a task identifier before the video is ready.]

## Skill Version(s):

1.3.33 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
