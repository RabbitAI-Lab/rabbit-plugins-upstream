## Description:

Creates 15–25-second vertical social videos with a hook-led storyboard, generated shots, voiceover, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social media teams use this skill to produce short, vertical videos for TikTok, YouTube Shorts, Reels, and similar platforms rather than receiving only a script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files provided for video generation are sent to dLazy's hosted service.

Mitigation: Only submit content you are authorized to share, and confirm you trust the dLazy service before use.

Risk: The dLazy CLI stores an API key locally after login.

Mitigation: Protect the local key and rotate or revoke it through dLazy if needed.

Risk: Installing the third-party dLazy CLI adds software to the user's environment.

Mitigation: Review the pinned CLI before installation; use the documented npx invocation to avoid a global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [15–25-second vertical MP4 and streamed text response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [9:16 video with voiceover and burned-in subtitles]

## Skill Version(s):

1.2.33 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
