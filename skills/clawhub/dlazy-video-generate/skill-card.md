## Description:

视频生成技能，AI 视频生成，文生视频、图生视频、图片转视频、首尾帧生成视频。根据提示词自动选择最佳视频生成模型（即梦、可灵、Veo、Seedance、万相、PixVerse、数字人、对口型）。Video generation skill that automatically selects the best dlazy CLI video model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform videos through the dLazy CLI, including text-to-video, image-to-video, first/last-frame video, reference-guided video, digital human video, lip sync, and related video utilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy cloud endpoints for generation.

Mitigation: Use the skill only with content that is appropriate for the dLazy cloud service and avoid sending sensitive media unless that use is approved.

Risk: The skill relies on a pinned npm CLI package and may be installed globally.

Mitigation: Prefer the pinned npx invocation for temporary use, or review the package and source before global installation.

Risk: dLazy API keys authorize access to the user's organization and may be stored in local CLI configuration.

Mitigation: Protect local CLI configuration, use environment-scoped credentials when appropriate, and rotate or revoke keys when access is no longer needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and references to JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI returns JSON envelopes that can be piped between commands; generated media URLs are returned by the dLazy service.]

## Skill Version(s):

1.4.15 (source: server release metadata; artifact frontmatter reports 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
