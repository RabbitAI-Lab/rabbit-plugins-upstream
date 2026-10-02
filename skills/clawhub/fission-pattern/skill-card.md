## Description:

Turns a reference product image and selling points into prompts and commands for a consistent set of e-commerce product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use the skill to plan and generate multiple product views and lifestyle scenes from a reference image while keeping product details consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product or reference images are sent to the configured image provider.

Mitigation: Use an approved provider and avoid private or sensitive images unless that provider is authorized to process them.

Risk: Generating a multi-image set can incur repeated provider charges.

Mitigation: Use dry-run to review requests and estimated costs before generating the set.

Risk: Generated views may misrepresent product details or introduce unsupported claims.

Mitigation: Compare each generated image against the reference and supplied selling points before publication; regenerate inaccurate images.

Risk: Provider API keys grant access to paid image-generation services.

Mitigation: Keep keys scoped and revocable, and do not include them in prompts or shared files.

## Reference(s):

- [Fission Pattern release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with image-generation prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated product images locally; image format, dimensions and quality are configurable.]

## Skill Version(s):

1.0.16 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
