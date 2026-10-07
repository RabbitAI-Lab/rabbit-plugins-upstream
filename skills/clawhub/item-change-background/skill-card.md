## Description:

Places product photos into realistic scenes while aiming to preserve product details and match lighting, reflections, and shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketers use this skill to place product photos into realistic lifestyle scenes or supplied backgrounds for listings and promotional imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and optional background images are sent to the configured cloud provider.

Mitigation: Use a dry run to inspect the request, avoid sensitive unreleased assets unless provider terms allow them, and keep API keys scoped and revocable.

Risk: Generated scenes may alter product details or imply misleading uses.

Mitigation: Compare each result with the original product and review scene plausibility before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, saves generated product images locally; a dry run previews the request without generation.]

## Skill Version(s):

1.0.17 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
