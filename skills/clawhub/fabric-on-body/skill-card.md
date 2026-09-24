## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and apparel teams use this skill to preview a garment pattern or style sheet rendered in a different fabric before physical sampling. It helps agents compose prompts, validate inputs, and run image-generation commands that preserve garment structure while changing material appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment and fabric images are uploaded to the selected image-generation provider.

Mitigation: Use only images intended for sharing with that provider, avoid sensitive photos and internal URLs, and review the provider's data handling before execution.

Risk: Provider API keys are required for some backends.

Mitigation: Use scoped, revocable keys and keep credentials out of prompts, command history, and shared files.

Risk: Generation can consume credits or paid provider quota.

Mitigation: Run dry-run first to inspect the request and estimated cost before making paid calls.

Risk: Generated garment previews can misrepresent physical fabric properties.

Mitigation: Treat outputs as visual previews only and verify hand feel, weight, drape, and construction through normal sampling or review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [Example style sheet image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/style-sheet.jpg)
- [Example fabric swatch image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/fabric-swatch.jpg)
- [Example generated output](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/fabric-on-body/example-output.jpg)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with bash command examples, prompt templates, provider configuration, and generated image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces visual previews only; generated images are not physical fabric samples or guarantees of real-world hand feel, weight, or construction.]

## Skill Version(s):

1.0.13 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
