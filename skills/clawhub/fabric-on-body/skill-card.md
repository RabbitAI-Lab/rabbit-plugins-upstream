## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion, ecommerce, and product teams use this skill to preview how a garment style sheet would look when rendered in a new fabric before physical sampling. It helps agents prepare fabric-replacement prompts, commands, and quality checks while treating the result as a visual preview rather than a physical sample.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected garment or fabric images are uploaded to the configured image provider during generation.

Mitigation: Use only images approved for that provider and review the provider's data handling before running generation.

Risk: Generated fabric previews may not reflect real hand-feel, weight, construction fidelity, or exact drape.

Mitigation: Treat outputs as visual previews and verify important production decisions against physical samples or product expertise.

Risk: Optional brand templates can encode unsuitable modeling or representation requirements.

Mitigation: Edit brand templates to match the user's brand, modeling, and representation requirements before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image outputs are typically JPEG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a garment style image and a fabric swatch image as inputs; saved output paths are provided when generation runs.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
