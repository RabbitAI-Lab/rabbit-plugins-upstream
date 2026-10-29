## Description:

Storyboard script generator, taking user-provided themes, structured copy (such as a script containing hooks, suspense, story development, core viewpoints), or outlines, dismantling them into detailed short video storyboard scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and script writers can provide a theme, structured copy, or outline and receive a detailed short-video storyboard that preserves their original spoken copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promises text-only storyboard output but also includes an external image-generation workflow that uses account credentials and cloud uploads.

Mitigation: Prefer a corrected, consistent text-only workflow. For image generation, explicitly approve CLI execution, transfer of prompts or selected media, and possible charges; use a revocable dLazy key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown storyboard script with video parameters and numbered shot descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves supplied spoken copy word for word; defaults to 9:16 and 720p when video parameters are absent.]

## Skill Version(s):

1.2.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
