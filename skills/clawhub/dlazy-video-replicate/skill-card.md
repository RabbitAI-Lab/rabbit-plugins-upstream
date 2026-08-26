## Description:

Video Replicate extracts the first frame and audio from a source video, uses video understanding to generate a prompt, and returns a Seedance 2.0 replicate bundle with first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent operators use this skill to replicate the structure of a source video by sending selected video inputs to the dLazy CLI and receiving generated media outputs. It is useful when an agent needs to prepare or run a video-replication generation workflow from command-line inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, audio, images, prompts, and generation parameters are sent to dLazy for processing.

Mitigation: Use the skill only with media and prompts that are appropriate to share with dLazy, and review organizational data-handling requirements before execution.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use per-invocation environment variables or the pinned npx command when persistence is not desired, and rotate or revoke the key from dLazy if exposure is suspected.

Risk: A global CLI install increases the amount of software retained on the system.

Mitigation: Prefer the pinned npx invocation, npx @dlazy/cli@1.2.3, when a persistent global CLI is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Files]

**Output Format:** [JSON results with generated media URLs, task status for asynchronous runs, and optional downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local video, audio, or image inputs may be uploaded to dLazy for processing.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
