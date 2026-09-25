## Description:

Edits an existing model or mannequin e-commerce photo to replace the model, the background, or both while keeping the product unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and commerce creative teams use this skill to create multiple audience and scene variants from one existing product-on-model image while preserving the garment or product presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded product or model photos and prompts may be sent to the selected cloud image provider.

Mitigation: Use only provider accounts you trust and avoid sensitive, private, or unauthorized personal images.

Risk: Generated assets are written to local output paths selected by the user or command.

Mitigation: Choose output paths deliberately and review generated files before publishing or sharing them.

Risk: Model or background replacement can be misused to imply identity, endorsement, or authorization that does not exist.

Mitigation: Do not use the skill to swap in a specific real person, forge endorsements, or create unauthorized likeness-based advertising.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with command examples and local image file outputs when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt text, ordered image inputs, model/provider options, output path settings, and optional batch generation.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
