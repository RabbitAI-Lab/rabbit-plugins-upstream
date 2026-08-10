## Description:

Creates hook-first 15-25 second vertical short videos with storyboard, first frames, image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted short-video workflow for social vertical videos such as TikTok, YouTube Shorts, Instagram Reels, Douyin, and talking-head shorts. It is intended to produce a finished MP4 rather than only a script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service for processing.

Mitigation: Avoid sending confidential or regulated data unless the dLazy service terms and the user's organization permit it.

Risk: Authentication stores a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate, protect the local config file, and rotate or revoke the key from dLazy if it may be exposed.

Risk: Using a globally installed CLI leaves a persistent executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying service may produce or reference a finished 15-25 second vertical MP4.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
