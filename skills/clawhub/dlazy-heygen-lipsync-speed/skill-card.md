## Description:

Helps agents generate lip-synced media quickly from video and audio inputs using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request fast lip-sync generation from video and audio inputs through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Execution depends on the third-party @dlazy/cli package.

Mitigation: Review the package before installing or running it.

Risk: Video and audio files supplied as local paths are uploaded to dLazy.

Mitigation: Only provide media approved for upload to that service.

Risk: CLI login or manual key setup stores an API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY when persistent local storage is unwanted.

Risk: Some documented examples do not match the lip-sync command options.

Mitigation: Check the command's help and confirm flags before running examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (dependency listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON]

**Output Format:** [CLI command guidance and JSON responses with result URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be downloaded to a local path when requested.]

## Skill Version(s):

1.3.31 (source: server-resolved release; bundled frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
