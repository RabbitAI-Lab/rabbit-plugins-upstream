## Description:

Helps agents use dLazy to analyze a source video and obtain a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare a video-replication workflow from source footage, including a first frame, audio, and a descriptive prompt for Seedance 2.0.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source media submitted to the dLazy cloud service may contain sensitive content.

Mitigation: Submit only media files you intend to upload to dLazy.

Risk: Authentication may leave an API key in the local CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY authentication when local key storage is unsuitable.

Risk: Installing the CLI runs a third-party package.

Mitigation: Review the pinned @dlazy/cli package and its listed source before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can include generated media URLs; asynchronous requests can return a task ID for polling.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
