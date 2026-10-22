## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers, apparel product teams, and e-commerce creators use this skill to preview how a garment pattern may look in a selected fabric before sampling. The generated image is a visual preview, not a physical sample or a guarantee of fabric hand, weight, or construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images and prompts are sent to the selected cloud provider for generation.

Mitigation: Choose a provider whose data-handling terms are acceptable and do not upload confidential designs unless permitted.

Risk: Saving generated files to an existing path could overwrite important work.

Mitigation: Use --dry-run to check the destination and inputs, and choose a new or otherwise safe output path before a paid run.

Risk: Generated previews may not accurately represent physical fabric, fit, or construction.

Mitigation: Treat results as visual concepts and verify fabric properties and garment construction with physical samples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [Generated garment fabric-change preview images, JPEG by default; available formats depend on the selected provider and model.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; generated appearance can differ from physical fabric properties. Provider choice, image dimensions, quality, format, batch size, and save path may be configured.]

## Skill Version(s):

1.0.25 (source: SKILL.md frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
