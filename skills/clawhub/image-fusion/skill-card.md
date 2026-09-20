## Description:

This skill helps agents generate ecommerce fashion look images by combining up to eight product images into one outfit on the same model while preserving each item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and developers use this skill to produce consistent product styling images from multiple apparel or accessory references. It guides prompt construction, image ordering, provider selection, dry runs, and quality checks for multi-item outfit fusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product, model, and reference images plus prompts may be sent to the configured cloud generation provider.

Mitigation: Use only providers approved for the intended data, avoid private or sensitive images, and set --provider explicitly when provider choice matters.

Risk: A generation command can incur provider credits or produce unintended output if run with the wrong settings.

Mitigation: Run with --dry-run first to inspect the payload and expected provider behavior before executing paid generation.

Risk: Generated fashion images may fail to preserve every item exactly or could be misused to imply a person's endorsement.

Mitigation: Review outputs for item fidelity, layer ordering, likeness handling, and use-case appropriateness before publication.

## Reference(s):

- [Provider CLI reference](artifact/references/provider-cli.md)
- [seedream-5.0 model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, CLI command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are produced by the configured cloud image provider when the emitted commands are executed.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
