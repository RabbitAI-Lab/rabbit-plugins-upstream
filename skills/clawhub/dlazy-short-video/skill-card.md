## Description:

Creates 15–25-second vertical social videos with a storyboard, voiceover, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use this skill to produce finished short-form vertical videos for TikTok, YouTube Shorts, Instagram Reels, and Douyin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the external dLazy service, and attached files are uploaded to its storage.

Mitigation: Review prompts and attachments before sending; avoid private files unless their transfer is intended.

Risk: Login saves a dLazy API key locally.

Mitigation: Protect access to the local configuration or supply the key per invocation; rotate or revoke compromised keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI repository (publisher-provided link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Vertical MP4 video and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [15–25 seconds; voiceover and burned-in subtitles.]

## Skill Version(s):

1.2.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
