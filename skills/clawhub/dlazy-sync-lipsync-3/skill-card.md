## Description:

fal.ai sync-lipsync v3 generates a new video from input video and audio where the speaker's lip movement matches the audio for dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to invoke dLazy's hosted sync-lipsync-3 workflow for lip-syncing an input video to a separate audio track. It supports dubbing, localization, and re-syncing virtual presenters through CLI commands and optional saved media output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video and audio files are uploaded to dLazy hosted endpoints for processing.

Mitigation: Confirm the selected media is appropriate to upload to dLazy before running the command, and use dry-run when validating parameters.

Risk: The workflow requires a dLazy API key that may be stored locally or passed through an environment variable.

Mitigation: Use OS-user-restricted config permissions, avoid exposing the key in logs or prompts, and revoke or rotate the key if exposure is suspected.

Risk: A third-party CLI is required to execute the skill.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global install is not needed, and review the published CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or a saved generated media file when requested.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
