## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 -> 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators, merchandisers, and developers use this skill to compose shoes, bags, watches, eyewear, hats, scarves, necklaces, earrings, and similar accessories onto consenting model/reference images for product photography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, model/reference images, prompts, and generation requests may be sent to external provider services.

Mitigation: Use only appropriate, consented, non-sensitive images and review the selected provider's data handling terms before running the skill.

Risk: Provider credentials and endpoint configuration are required for generation and could expose accounts if mishandled.

Mitigation: Use reviewed local CLI installations, store keys securely, rotate credentials when needed, and set ARK_BASE_URL only to trusted endpoints.

Risk: The release security summary flags under-scoped agent/run instructions.

Mitigation: Run dry-run first, inspect commands and payloads before execution, and avoid ad hoc npm or npx execution paths when a reviewed local CLI is available.

Risk: On-model accessory images can imply endorsement or identity use if reference people are not authorized.

Mitigation: Use consenting model/reference images and avoid prompts or outputs that falsely imply personal endorsement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell command examples and saved image files from generation tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are typically JPEG outputs; dry-run mode can emit request and cost previews before paid generation.]

## Skill Version(s):

1.0.9 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
