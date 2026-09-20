## Description:

Video replicate tool that extracts the first frame and audio from a source video, runs video understanding to generate a prompt, and returns a Seedance 2.0 replicate bundle with first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to invoke the dLazy cloud CLI for video replication workflows that derive a first frame, audio, and descriptive prompt from a reference video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and video, audio, or image inputs may be uploaded to the third-party dLazy cloud service.

Mitigation: Use this skill only with media and prompts approved for dLazy processing, and prefer dry-run or review steps before submitting sensitive content.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY or npx when less local persistence is preferred, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes that may include media file URLs or saved assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; local media paths may be uploaded to dLazy and asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
