## Description:

Creates short-video storyboard scripts from supplied copy and also guides confirmed image generation using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video teams use this skill to turn themes, outlines, and existing copy into shot-by-shot scripts with camera directions and intact spoken text. It also offers a user-confirmed path to generate images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as text-only but also directs the agent to install and run a networked image-generation CLI.

Mitigation: Review the CLI before installation and require explicit user confirmation before running image-generation commands.

Risk: Using the CLI stores an API key locally and sends prompts or referenced media to dLazy services.

Mitigation: Use a scoped, revocable key and send only content the user approves for external processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI repository (tool reference, not skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown storyboard with per-shot scenes and spoken scripts; optional image-generation commands and result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves supplied spoken copy verbatim; defaults to 9:16 and 720p when unspecified.]

## Skill Version(s):

1.2.22 (source: ClawHub release metadata; skill frontmatter states 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
