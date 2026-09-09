## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle with first-frame, audio, and video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to run dLazy's video-replicate workflow for turning a source video into a Seedance 2.0 replication bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a pinned third-party dLazy CLI package.

Mitigation: Review the linked dLazy CLI source or npm package before installation in sensitive environments, and prefer the pinned npx invocation when avoiding a persistent global install.

Risk: The workflow requires a dLazy API key and may store credentials in the local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Videos, audio, prompts, and generated outputs may be sent to or hosted by dLazy's cloud service.

Mitigation: Only pass media and prompts approved for upload to dLazy's hosted service, especially when handling sensitive or proprietary content.

## Reference(s):

- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, async task identifiers, or saved local assets when the save option is used.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
