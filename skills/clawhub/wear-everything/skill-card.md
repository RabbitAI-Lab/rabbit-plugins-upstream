## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce content creators use this skill to generate photorealistic on-model accessory images from product photos and model references. It provides prompt templates, placement guidance, CLI commands, and quality checks for shoes, bags, eyewear, jewelry, hats, scarves, and similar accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model or reference photos, prompts, and output requests may be sent to dLazy or another configured provider.

Mitigation: Use only approved providers, review configured credentials, and avoid sensitive private images unless provider data handling is approved for the use case.

Risk: Non-Chinese readers may miss workflow constraints because much of the skill documentation is in Chinese.

Mitigation: Have a fluent reviewer or translation process confirm the workflow, prompts, and safety constraints before operational use.

Risk: On-model generated imagery can imply identity use or endorsement if real people are used without rights.

Mitigation: Use authorized model/reference images and do not use outputs to fabricate personal endorsements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with prompt templates, tables, and inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to call configured image-generation providers and save JPEG outputs; generated images are produced by those external provider calls.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
