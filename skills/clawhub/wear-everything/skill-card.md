## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce content teams use this skill to generate on-model product photos that place shoes, bags, watches, glasses, hats, scarves, jewelry, and similar accessories onto a human model reference image while preserving product details and scene context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model/reference photos, and prompts are sent to the selected cloud image provider.

Mitigation: Review the configured provider and API key before use, avoid sensitive images unless the provider is acceptable, and run dry-run or doctor mode first when possible.

Risk: Unpinned install suggestions can change the installed CLI source over time.

Mitigation: Review or pin the CLI source before following install commands from GitHub.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation calls that produce JPEG product imagery through a selected cloud image provider.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
