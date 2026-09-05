## Description:

Creates and applies a reusable brand.yaml so ecommerce image-generation workflows keep models, lighting, composition, whitespace, and copy tone visually consistent across many SKUs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, designers, and agentic image-generation workflows use this skill to create or apply a shared brand.yaml. The brand file lets related image skills reuse the same visual constraints for model identity, art direction, photography, layout, forbidden elements, and platform compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected images, and referenced URLs may be sent to cloud model providers.

Mitigation: Use --dry-run before paid or remote runs, pass only intended local files or trusted URLs, and avoid including sensitive source material unless the selected provider is approved for it.

Risk: Default brand templates include model demographics and visual assumptions that may not fit the user's brand or compliance needs.

Mitigation: Edit brand.yaml before generation, especially model, photography, forbid, and compliance fields, then test one SKU before running a batch.

Risk: Image-generation runs can consume provider credits.

Mitigation: Check the selected provider and estimated credits with --dry-run or --doctor before executing full generation jobs.

Risk: A missing model reference image reduces face-consistency behavior while allowing generation to continue.

Mitigation: Confirm model.reference points to an existing, clear face image before using the brand file for production batches.

## Reference(s):

- [brand.yaml field reference](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML configuration and shell command examples; helper scripts can also emit JSON reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can append prompt constraints, include selected local or URL reference images, estimate provider credits during dry runs, and save generated image outputs when invoked through gen.mjs.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
