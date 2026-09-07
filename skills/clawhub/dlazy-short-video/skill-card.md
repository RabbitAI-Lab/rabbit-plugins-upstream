## Description:

Generates hook-first 15-25 second vertical short videos with storyboarded shots, first-frame and image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to generate social-media-ready vertical short videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar channels. It is intended for finished social shorts rather than scripts or conversion-focused product ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a dLazy API key and may store it in the local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when persistence is not desired, and rotate or revoke the key when it is no longer needed or may have been exposed.

Risk: Files attached with the CLI are uploaded to dLazy media storage before use.

Mitigation: Attach only files that are intended for upload to dLazy and review sensitive content before invoking file-based workflows.

Risk: Installing a persistent global CLI package can increase supply-chain and local-environment exposure in sensitive environments.

Mitigation: Prefer the pinned npx @dlazy/cli@1.2.3 invocation for temporary use and review the CLI source or package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Terminal text and generated 15-25 second vertical MP4 video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI package @dlazy/cli@1.2.3 and can continue work by project id.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
