## Description:

Creates finished 15-25 second vertical social videos with hook-first storyboards, per-shot first frames and image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to generate short vertical social videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, Xiaohongshu, and similar channels. It is intended for social shorts rather than conversion-focused product advertisements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and attached files may be sent to dLazy's hosted service.

Mitigation: Use only organization-approved content and avoid attaching confidential files unless that data flow is approved.

Risk: The dLazy CLI can persist an API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when persistent local credentials are undesirable, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Terminal text and shell commands; generated media is a vertical MP4.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; optional local files can be attached through the CLI and uploaded for use as references.]

## Skill Version(s):

1.2.11 (source: server release metadata; artifact frontmatter reports 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
