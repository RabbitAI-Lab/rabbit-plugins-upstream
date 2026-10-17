## Description:

Creates shot-by-shot short-video storyboard scripts from a user's theme, outline, or structured copy while preserving the supplied spoken text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and production teams use this skill to turn themes, outlines, or structured copy into shootable short-video storyboards with scene, camera, and spoken-script details. An optional image-rendering workflow uses a third-party service after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises text-only storyboards but can also install and run a third-party image-generation CLI.

Mitigation: Use the text-only workflow unless external rendering is wanted; review the CLI and confirm before installing or running it.

Risk: Rendering requires API authentication and may send prompts and media files to dLazy services.

Mitigation: Obtain consent before sending content, avoid sensitive inputs, and keep API credentials private.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands]

**Output Format:** [Markdown storyboard with video parameters and numbered shots; optional image-generation commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each shot includes scene, camera movement, shooting notes, technique, and verbatim spoken copy; default video settings are 9:16 and 720p.]

## Skill Version(s):

1.2.26 (source: server-resolved ClawHub release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
