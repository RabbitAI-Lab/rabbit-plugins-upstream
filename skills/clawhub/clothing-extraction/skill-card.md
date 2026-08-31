## Description:

Extracts clean e-commerce flat-lay clothing images from model, street-style, buyer, or product-reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators, merchandisers, and developers use this skill to turn worn, street-style, buyer, or competitor reference photos into clean product flat-lay images. It helps prepare garment inputs for product listings, 3D workflows, try-on workflows, and related image-generation pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to dLazy or another configured image provider.

Mitigation: Use only images and prompts that are appropriate to share with the selected provider, and avoid sensitive personal photos or confidential buyer images.

Risk: Reference photos may include competitor, copyrighted, branded, or consent-sensitive material.

Mitigation: Confirm rights, consent, and permitted use before processing source images or publishing generated flat-lay outputs.

Risk: Occluded garment areas are reconstructed rather than directly observed.

Mitigation: Review saved output files for fidelity, especially around blocked design details, before using them in product listings or downstream workflows.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [ClawHub Skill Listing](https://clawhub.ai/dlazyai/skills/clothing-extraction)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt templates, command examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can save generated image files locally through the configured image provider.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
