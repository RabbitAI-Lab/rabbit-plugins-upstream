## Description:

Helps e-commerce teams maintain consistent product imagery by applying a shared brand configuration for model references, lighting, composition, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creative operators use a shared brand configuration to keep product visuals consistent across SKUs and image-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to a cloud generation provider.

Mitigation: Choose the provider explicitly, preview requests with --dry-run, and avoid sensitive images or untrusted/internal image URLs.

Risk: Generation requires provider credentials and can incur charges.

Mitigation: Keep API keys in normal environment or CLI credential stores and check the planned request with --dry-run before generating.

## Reference(s):

- [Brand Kit release on ClawHub](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](references/brand-schema.md)
- [Generation provider and CLI guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Configuration, Shell commands]

**Output Format:** [Brand YAML or JSON and task-specific prompt text; shell commands can generate product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional model reference image and provider selection; image-generation results depend on the chosen cloud provider.]

## Skill Version(s):

1.0.15 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
