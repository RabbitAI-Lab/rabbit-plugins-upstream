## Description:

Creates images from scene descriptions and supports targeted edits to a reference image's model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to generate scenes from text or edit supplied images to change a model, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images may be sent to the selected cloud provider.

Mitigation: Use non-sensitive inputs and confirm the selected provider and active credentials before running.

Risk: Generation requests may incur charges or save images to an unintended location.

Mitigation: Review the request and cost with --dry-run, then choose the output path deliberately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Image model options](references/model-flags.md)
- [Provider setup and output guide](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Prompt guidance]

**Output Format:** [Generated image files and text or Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images and user-selected output paths.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
