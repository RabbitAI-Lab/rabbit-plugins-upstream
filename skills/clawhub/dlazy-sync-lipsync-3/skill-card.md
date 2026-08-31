## Description:

fal.ai sync-lipsync v3 generates a new video from an input video and audio track so the speaker's lip movement matches the audio for dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted sync-lipsync-3 service for video lip synchronization with supplied video and audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy-hosted services for cloud processing.

Mitigation: Use the skill only with media that is approved for upload to dLazy services, and review dLazy service terms before processing sensitive or regulated content.

Risk: A dLazy API key may be stored locally in the user's CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses containing hosted output URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated video to a local path when the CLI is invoked with --save.]

## Skill Version(s):

1.3.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
