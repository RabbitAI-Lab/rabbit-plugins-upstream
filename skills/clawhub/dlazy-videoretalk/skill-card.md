## Description:

Video Retalk lip-syncs a talking-person video to a supplied voice audio track, with an optional reference face image to select the target person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted VideoRetalk service for generating a video whose mouth movements match a new audio track. It is useful for dubbing and lip-sync workflows where the user supplies the source video and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI to call a hosted dLazy service.

Mitigation: Use the pinned CLI version, prefer npx or another contained install when appropriate, and review the package before installing globally.

Risk: Video, audio, and optional image inputs may be uploaded to dLazy endpoints for processing.

Mitigation: Only provide media that is acceptable to process through the dLazy service and avoid sensitive inputs unless organizational policy allows it.

Risk: The evidence notes incorrect prompt-based usage examples in the artifact.

Mitigation: Use the documented --video_url and --audio_url options for VideoRetalk invocations.

Risk: The dLazy API key is a credential used by the CLI.

Mitigation: Protect the key, use the documented local config or DLAZY_API_KEY flow, and rotate or revoke it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return hosted output URLs or an asynchronous task identifier.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
