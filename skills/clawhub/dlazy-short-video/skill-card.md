## Description:

Short Video helps agents create 15-25 second vertical social videos with hook-first storyboards, image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy short-video projects that generate finished vertical videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar social channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI can introduce package and local execution risk.

Mitigation: Review the linked source or npm package before installation and avoid running npm installs as administrator or root.

Risk: Prompts and attached files may be sent to dLazy services.

Mitigation: Do not submit sensitive data without authorization, and review applicable service terms before use.

Risk: A stored API key could be misused if exposed.

Mitigation: Use a revocable dLazy API key, keep local config access restricted to the OS user, and rotate the key if compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [CLI text or Markdown guidance, with generated media expected as a vertical MP4 asset.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and attached files may be sent to dLazy services.]

## Skill Version(s):

1.2.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
