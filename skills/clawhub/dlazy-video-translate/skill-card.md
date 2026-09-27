## Description:

Transcribes video audio with word-level timings, translates subtitle cues, burns translated subtitles into an MP4, and optionally creates a timing-fitted dub track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, localization specialists, and content teams use this skill to translate video subtitles and optionally add a dubbed audio track while preserving source timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is uploaded to dLazy services and may contain sensitive audio or video content.

Mitigation: Review the service terms and avoid sending sensitive videos unless that processing is acceptable.

Risk: dLazy API calls may incur charges.

Mitigation: Use dry-run where available to estimate cost before spending credits.

Risk: An API key may be stored in the local dLazy CLI config.

Mitigation: Use DLAZY_API_KEY instead of saved config on shared machines, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated local media/subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates SRT subtitle files and MP4 video outputs; creates a dubbed audio track only when requested.]

## Skill Version(s):

1.0.12 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
