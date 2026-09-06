## Description:

Generates finished 15-25 second vertical short videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar social channels using storyboard, first-frame generation, image-to-video clips, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to run dLazy's hosted short-video template and produce social-ready 9:16 MP4 videos rather than only scripts or storyboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI can persist an organization-scoped dLazy API key in a local config file.

Mitigation: Prefer per-run DLAZY_API_KEY for sensitive environments, or verify and restrict permissions on ~/.dlazy/config.json after login.

Risk: Prompts and selected attachments are sent to dLazy services, including media storage for files passed with --files.

Mitigation: Review data sensitivity before use and avoid attaching confidential files unless dLazy handling is approved for the workflow.

Risk: The release security verdict is suspicious because the inspected CLI package does not clearly enforce the artifact's file-permission safety claim.

Mitigation: Review the third-party CLI before installing, use the pinned package version, and rotate or revoke the dLazy API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and hosted-agent responses that may include links or status for generated MP4 video output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI package @dlazy/cli@1.2.3 and the short-video hosted template; local attachments may be uploaded to dLazy media storage before generation.]

## Skill Version(s):

1.2.13 (source: server release evidence; artifact frontmatter reports 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
