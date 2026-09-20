## Description:

Creates finished 15-25 second 9:16 social short videos with hook-first storyboards, per-shot first frames and image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to start or continue dLazy projects that generate vertical social videos for TikTok, YouTube Shorts, Reels, Douyin, Xiaohongshu, and similar short-form channels. It is intended for social shorts rather than conversion-focused product advertisements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files passed with --files are uploaded to dLazy services.

Mitigation: Review prompts and attachments before use, avoid sending sensitive material unless approved, and follow the organization's data handling policy.

Risk: The dLazy API key is stored locally by the CLI and is required for all requests.

Mitigation: Use organization-scoped credentials, restrict local access to the config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists the @dlazy/cli executable on the user's system.

Mitigation: Review the package before installing or use the pinned npx invocation when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Terminal text with CLI commands and generated vertical MP4 video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses a project-scoped dLazy hosted agent; prompts and files supplied with --files may be sent to dLazy services.]

## Skill Version(s):

1.2.19 (source: server release metadata; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
