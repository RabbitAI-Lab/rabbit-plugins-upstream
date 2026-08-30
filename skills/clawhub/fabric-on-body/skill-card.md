## Description:

一键替换服装面料。版式图 + 面料图 -> 换上新面料的样衣图，垂坠与光泽随材质变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and apparel teams use this skill to preview how an existing garment style or pattern would look in a different fabric before physical sampling. It preserves the garment structure and camera layout while changing the visual material, weave, sheen, and drape.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, garment images, and fabric images are sent to dLazy or the configured image-generation provider.

Mitigation: Use the skill only with data approved for that provider, and avoid sensitive garment designs, private files, or internal-only URLs.

Risk: Generated previews can misrepresent physical properties such as fabric hand-feel, weight, or production feasibility.

Mitigation: Treat outputs as visual previews and verify final materials through normal sampling and production review.

Risk: Poor or mismatched inputs can produce inaccurate fabric color, texture, drape, or garment structure.

Mitigation: Use clear garment references and fabric swatches, follow the documented input constraints, and review generated images before relying on them.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces visual preview image assets, typically JPEG files; JSON envelopes are available when the generation wrapper is run with --json.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
