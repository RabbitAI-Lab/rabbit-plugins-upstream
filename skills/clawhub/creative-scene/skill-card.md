## Description:

Creates or edits commercial-style scene images from a short prompt, optionally using a reference image to change a model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft ecommerce or brand scene images from concise scene descriptions, then refine models, poses, outfits, framing, and visual tone with prompt templates and generated commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy or another configured image provider.

Mitigation: Use the skill only when that provider data flow is acceptable, and avoid sending sensitive or unauthorized images.

Risk: Generated images may be saved to unintended project paths.

Mitigation: Set explicit save paths and review output locations before running generation commands.

Risk: API keys are required for configured providers.

Mitigation: Keep provider keys scoped, revocable, and stored through the documented credential mechanisms.

Risk: Generated commercial imagery may be misleading if used as product evidence.

Mitigation: Review outputs before use and do not present generated images as real product photography or verified user experience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [banana-pro parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated JPEG or PNG image outputs locally; optional reference images can be used for targeted edits.]

## Skill Version(s):

1.0.1 (source: server evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
