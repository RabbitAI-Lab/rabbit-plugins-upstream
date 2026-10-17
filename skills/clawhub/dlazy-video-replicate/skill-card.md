## Description:

Uses a source video to generate a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide video replication from a reference video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and prompts are sent to dLazy's cloud service.

Mitigation: Use only media and prompts approved for upload to a third-party service.

Risk: Signing in or setting an API key can store credentials on the local machine.

Mitigation: Use an environment variable when local key storage is unsuitable, and rotate or revoke keys if needed.

Risk: Installing the external CLI globally persists it on the machine.

Mitigation: Use the pinned on-demand npx package if a global installation is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns asset URLs or an asynchronous task ID; generated media may include a first frame, audio, and video.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
