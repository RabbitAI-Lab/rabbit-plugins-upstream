## Description:

一键替换服装面料。版式图 + 面料图生成换上新面料的样衣视觉预览，垂坠与光泽随材质变化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce, fashion, and product-content teams use this skill to preview how an existing garment style sheet could look in a different fabric before sampling. The output is a visual preview for selection and review, not proof of physical hand feel, weight, or manufacturability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches, prompts, and generation parameters may be sent to dLazy or another configured cloud provider.

Mitigation: Use only approved input assets, confirm the selected provider and credentials, and run dry-run checks before submitting sensitive material.

Risk: Generated outputs can be mistaken for physical sampling results.

Mitigation: Label outputs as visual previews and require physical sampling or expert review for hand feel, weight, drape, and manufacturability decisions.

Risk: Low-quality swatches, color cast, complex original prints, or physically mismatched fabric/category pairs can produce misleading previews.

Mitigation: Use clear neutral-light swatches and simple style references, then review silhouette retention, material color, construction details, and fabric plausibility before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [Example garment style-sheet image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/style-sheet.jpg)
- [Example fabric swatch image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/fabric-swatch.jpg)
- [Example generated output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/example-output.jpg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with command examples and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces garment fabric-replacement visual previews from a garment style reference and fabric swatch; saved outputs are typically JPEG image files.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
