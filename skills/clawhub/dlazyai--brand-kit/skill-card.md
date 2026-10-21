## Description:

Helps keep ecommerce product imagery consistent across SKUs using a reusable brand specification for model appearance, lighting, composition, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and creative teams use a shared brand specification to guide consistent product imagery across multiple SKUs and generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation requests may disclose brand details, prompts, or reference images to the configured provider.

Mitigation: Inspect requests with --dry-run, avoid confidential images and internal URLs, and select a trusted provider.

Risk: A missing model reference image can weaken visual consistency without stopping generation.

Mitigation: Confirm reference image paths exist and review a sample SKU before generating a batch.

## Reference(s):

- [Brand Kit skill listing](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand specification fields](artifact/references/brand-schema.md)
- [Generation provider guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands, Guidance]

**Output Format:** [YAML or JSON brand specification and plain-text prompt constraints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation commands can use brand settings and a reference image to produce ecommerce imagery through a configured provider.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
