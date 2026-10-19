## Description:

Guides agents to use dLazy to analyze a source video and produce a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a reference video into a dLazy video-replication workflow and obtain a first frame, audio, and video for a Seedance 2.0 replication bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service.

Mitigation: Review media and service terms before sending sensitive or licensed content.

Risk: Authentication can store a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Installing the external CLI and running generation may incur cost.

Mitigation: Review the package and dLazy terms before installing; consider on-demand npx and a dry run to estimate costs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI repository (linked in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
