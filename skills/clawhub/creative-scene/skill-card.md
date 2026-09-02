## Description:

Generates creative scene images from a text prompt, optionally using a reference image to adjust the model, pose, styling, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creative operators, and developers use this skill to turn short product or scene descriptions into image-generation prompts and commands, including controlled edits for model appearance, pose, outfit, and brand-consistent styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to dLazy or another configured image provider.

Mitigation: Review prompts and reference images for sensitive content before execution, and use only approved provider credentials and accounts.

Risk: Generated files may be written to the requested save path.

Mitigation: Review the save path before running generated commands and inspect outputs before publishing or reusing them.

Risk: The sample brand template may contain fixed demographic defaults for generated images.

Mitigation: Edit or remove those defaults when they do not match the intended project, market, or compliance requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy product site](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands and optional generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated image files to the requested save path when commands are executed.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
