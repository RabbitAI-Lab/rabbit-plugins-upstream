## Description:

Turns storyboard details into a video-generation pipeline for placement on a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to arrange storyboard dialogue, scene imagery, and video prompts into a canvas-ready generation pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The storyboard workflow includes broader terminal-based image-generation instructions that may not match the requested task.

Mitigation: Review the proposed steps and authorize only commands and outputs needed for the storyboard.

Risk: CLI use sends prompts and uploaded media to dLazy cloud services.

Mitigation: Avoid sensitive inputs unless cloud processing is acceptable; review the CLI source or package before installation.

Risk: The CLI can retain an API key in local configuration, and the agent may execute terminal commands.

Mitigation: Prefer temporary DLAZY_API_KEY credentials on shared machines and review commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON configuration, Guidance, Shell commands]

**Output Format:** [JSON pipeline and canvas instructions, with optional terminal commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shared source audio and scene image; per-storyboard cloned audio and video nodes.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
