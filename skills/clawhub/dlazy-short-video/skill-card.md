## Description:

short video maker, tiktok video, youtube shorts, instagram reels, douyin video, vertical video, 9:16 video - hook-first single-thread storyboard, per-shot first frames and i2v clips, TTS voiceover, then Remotion assembles with burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to create short social videos through the dLazy short-video template, including storyboard, generated clips, TTS voiceover, assembly, and burned-in subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services when the CLI is used.

Mitigation: Attach only files intended for upload and review data-sharing expectations before use.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use normal OS account protections for the config file and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill depends on a third-party pinned npm package.

Mitigation: Confirm trust in dLazy and the pinned npm package before installing; use npx for one-off use when a global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to invoke the dLazy CLI and may result in a hosted dLazy project with a generated vertical MP4.]

## Skill Version(s):

1.2.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
