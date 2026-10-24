## Description:

Creates detailed short-video storyboard scripts from user-provided themes, outlines, or structured copy while preserving the supplied wording in spoken-script sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and video producers use the skill to turn a theme, outline, or structured copy into a detailed short-video storyboard, with the supplied copy distributed across spoken-script sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports conflicting instructions that pair a text-only storyboard task with mandatory cloud image generation, adding software, credential, and data-sharing requirements.

Mitigation: For text-only storyboards, use a version without mandatory rendering. Before any image generation, explicitly approve the dLazy CLI, submitted prompts or media, credential storage, and potential service charges.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [CLI project (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured Markdown storyboard with video parameters and per-shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes video aspect ratio, resolution, dimensions, and shot-level scene, action, and spoken-script details.]

## Skill Version(s):

1.2.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
