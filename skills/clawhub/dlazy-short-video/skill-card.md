## Description:

This skill helps agents use dLazy's hosted short-video workflow to create finished 15-25 second vertical MP4s with storyboarded shots, TTS voiceover, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to request social short-form videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar 9:16 channels. It is intended for finished social shorts rather than scripts or conversion-focused product ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy's hosted service.

Mitigation: Only attach files intended for upload and avoid submitting sensitive material unless dLazy's service terms and data handling are acceptable.

Risk: Authentication stores a dLazy API key locally for CLI use.

Mitigation: Use the documented login or key setup flow, protect the local config file, and rotate or revoke the organization key when access changes.

Risk: Installing the CLI globally leaves a persistent binary on the system.

Mitigation: Use the pinned npx command when a non-persistent invocation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with CLI commands and references to generated video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference a finished 15-25 second vertical MP4 through the dLazy hosted service.]

## Skill Version(s):

1.2.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
