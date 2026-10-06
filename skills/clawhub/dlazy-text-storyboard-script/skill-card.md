## Description:

Turns themes, structured copy, or outlines into shot-by-shot short-video storyboard scripts with camera directions and spoken lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn supplied copy into short-video shot lists with visual direction while preserving the original spoken text. The package also offers optional image generation through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Although advertised as a text storyboard helper, the skill may install or run a third-party CLI to generate images.

Mitigation: Review the package and proposed commands before installing or executing; use text-only output if image generation is not intended.

Risk: Image generation can send prompts and parameters to dLazy and upload referenced media files, with privacy and billing implications.

Mitigation: Confirm the intended data sharing and costs before use; avoid sensitive media and prefer per-run API keys when possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI repository (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown storyboard with video parameters, numbered shots, camera directions, and spoken scripts; optional CLI commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spoken lines preserve supplied copy; unspecified video settings default to 9:16 and 720p. Image generation requires separate user confirmation.]

## Skill Version(s):

1.2.21 (source: server release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
