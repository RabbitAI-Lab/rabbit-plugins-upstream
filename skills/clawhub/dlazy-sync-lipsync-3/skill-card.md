## Description:

Generates a lip-synced video from an input video and audio using fal.ai sync-lipsync v3 for dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted lip-sync video generation service from an agent. It supports dubbing, localization, and virtual presenter re-syncing workflows that provide video and audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided video and audio may be uploaded to dLazy's hosted service and generated results are hosted by dLazy.

Mitigation: Use only media approved for cloud processing and review dLazy service terms and data-handling expectations before use.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Prefer per-invocation environment variables when persistence is not desired, protect local config permissions, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install can persist executable code on the user's system.

Mitigation: Use the pinned npx invocation when a temporary install is preferred, or review the dLazy CLI package before global installation.

Risk: The artifact includes documentation quality issues where some examples do not match the video and audio flags for this model.

Mitigation: Use `dlazy sync-lipsync-3 -h` as the operational reference and provide `--video_url` and `--audio_url` inputs for real invocations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful CLI invocations return hosted generated media URLs and can save output files when requested.]

## Skill Version(s):

1.3.20 (source: evidence.release.version; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
