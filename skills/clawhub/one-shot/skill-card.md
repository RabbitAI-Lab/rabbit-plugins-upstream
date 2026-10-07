## Description:

Helps e-commerce teams create model and background variations from an existing product photo while aiming to preserve the product's appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to plan and run edits that replace a model, a background, or both in existing product imagery for different audiences and settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or model images and prompts are sent to the configured image-generation provider.

Mitigation: Use only images you are comfortable sharing with that provider; review the selected provider and API key before execution.

Risk: Generation requests may incur costs or use unintended settings.

Mitigation: Run --dry-run to review the request and estimated cost before generating images.

Risk: An example brand profile may carry unsuitable model demographics into new campaigns.

Mitigation: Customize the example profile for the intended audience instead of using its demographics as defaults.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can generate and save edited product images locally; inspect outputs for product fidelity.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
