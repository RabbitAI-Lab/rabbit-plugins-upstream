## Description:

A structured skill for planning and generating platform-adapted social media visuals and layered caption copy for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan social-media image concepts, platform-specific layouts, in-image text, caption copy, and dLazy CLI generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs or installs third-party dLazy npm CLI code.

Mitigation: Prefer the npx path or a sandboxed environment, and review the intended CLI package before use.

Risk: Prompts and selected media files may be sent to dLazy services for generation.

Mitigation: Avoid uploading sensitive local files or confidential prompts unless that transfer is acceptable.

Risk: The dLazy API key may be stored locally by the CLI.

Mitigation: Use a dedicated revocable API key and rotate or revoke it from the dLazy dashboard when needed.

Risk: Evidence notes a version mismatch between the intended CLI version and stray provenance text.

Mitigation: Verify the CLI version to run before installation or execution, with preference for the pinned 1.2.3 commands in the artifact metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, text, markdown]

**Output Format:** [Markdown with planning notes, prompt drafts, CLI commands, captions, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform specification checks, safe-area checks, layout plans, in-image text, caption copy, and iteration suggestions.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
