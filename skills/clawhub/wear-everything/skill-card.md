## Description:

Generates on-model commercial images that place shoes, bags, and accessories from product photos onto a model reference while preserving placement, perspective, shadows, and product fidelity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, product photographers, and developers use this skill to create catalog or marketing images where accessories are realistically worn by a model while the source product remains faithful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images may be sent to the selected image provider.

Mitigation: Use dry-run and provider selection before paid generation runs, and only submit prompts or images that are acceptable for the selected provider.

Risk: Broad URL fetching can expose the workflow to untrusted image URLs.

Mitigation: Prefer local trusted image files and avoid untrusted remote image URLs.

Risk: A custom Ark endpoint could receive an Ark API key if configured.

Mitigation: Do not set ARK_BASE_URL unless it points to a trusted HTTPS enterprise gateway.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with CLI examples, prompt templates, configuration notes, and generated image file paths or URLs when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product image inputs and a model reference image; supports provider selection, dry-run checks, batch generation, and local save paths.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
