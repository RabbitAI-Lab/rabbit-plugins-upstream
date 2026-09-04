## Description:

This skill helps agents prepare e-commerce image-editing prompts and commands that replace the model, background, or both while keeping the product unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and developers use this skill to create localized catalog-image variants from existing model or mannequin photos for different scenes, ages, skin tones, and markets while preserving the garment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided product and model images may be sent to the selected cloud provider.

Mitigation: Use the skill only with images the user has rights and consent to process, and require explicit approval or a provider allowlist for regulated, private, or identity-sensitive photos.

Risk: Demographic model replacement can create consent, representation, or endorsement concerns.

Mitigation: Confirm rights and consent for model imagery and requested demographic changes, and avoid using outputs to imply a real person's endorsement or identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 parameter reference](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Flat-lay comparison skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Material enhancement follow-up skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, prompt templates, and CLI options; invoked providers may save generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied source images and optional reference images; batch generation and local save paths are controlled by CLI flags.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
