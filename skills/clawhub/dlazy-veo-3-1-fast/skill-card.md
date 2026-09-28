## Description:

Generates short videos from text or images and extends videos using Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text or image prompts, or extend an existing video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media can be sent to dLazy's hosted service.

Mitigation: Use only media and prompts approved for third-party cloud processing.

Risk: Login can store a dLazy API key on the local machine.

Mitigation: Protect the local account and rotate or revoke the key if exposed.

Risk: Using the skill installs or runs an external CLI package.

Mitigation: Review the package and source before use; prefer the pinned on-demand invocation when a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with generated-video links and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a task ID for asynchronous completion; videos can be saved locally.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
