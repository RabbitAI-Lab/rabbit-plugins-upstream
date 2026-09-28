## Description:

Defines reusable brand guidelines for consistent model appearance, lighting, composition, layout, and tone across store product visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and creative teams use a shared brand configuration to keep product imagery and copy direction consistent across SKUs. The skill can turn that configuration into generation prompts and optionally create images with a selected cloud provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation sends prompts and selected product or model images to an external provider.

Mitigation: Review the provider's data handling and avoid submitting confidential images unless acceptable.

Risk: Brand defaults or batch settings may create unintended imagery or paid generation requests.

Mitigation: Review brand.yaml, remove unwanted demographic defaults, and use --dry-run before batch generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](references/brand-schema.md)
- [Image provider guidance](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands, Images]

**Output Format:** [YAML or JSON brand settings, prompt text, and optional generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific constraints and an optional model reference image can be added to generation requests.]

## Skill Version(s):

1.0.12 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
