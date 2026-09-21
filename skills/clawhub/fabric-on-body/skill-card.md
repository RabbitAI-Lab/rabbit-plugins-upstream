## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion ecommerce teams and apparel designers use this skill to preview how an existing garment silhouette would look in a new fabric before physical sampling. It guides an agent to prepare inputs, generate fabric-replacement images, save outputs, and quality-check the visual preview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, fabric references, and prompts may be sent to dLazy or another configured cloud image provider.

Mitigation: Avoid sensitive body photos, private or internal URLs, and secrets in prompts; choose the provider deliberately before generation.

Risk: Paid generation may run against the selected provider and save files to the requested output path.

Mitigation: Use dry-run mode before execution and review the provider, save path, image inputs, and batch settings.

Risk: Generated results are visual previews and may not reflect real textile hand feel, weight, or production behavior.

Mitigation: Use outputs for pre-sampling visualization only and validate fabric properties through normal sampling or production review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [gpt-image-2 parameter list](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Fabric replacement example output](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands and locally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces visual fabric-replacement previews from garment and fabric reference images; outputs are previews, not physical fabric samples.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
