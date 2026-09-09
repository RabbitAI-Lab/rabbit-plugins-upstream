## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketplace teams, and ecommerce operators use this skill to generate on-model accessory product imagery from product photos and model or scene references. It focuses on shoes, bags, watches, eyewear, hats, scarves, jewelry, belts, gloves, and similar wearable accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product or model images may be sent to dLazy or another configured provider.

Mitigation: Use the skill only with images and prompts that are acceptable to share with the selected provider, and review the configured provider before execution.

Risk: The skill can execute image-generation commands and supports configurable execution or network endpoints.

Mitigation: Run `--dry-run` first, avoid untrusted image URLs, do not set `DLAZY_BIN` or `ARK_BASE_URL` unless the executable or endpoint is trusted, and prefer pinned or verified CLI installation methods.

Risk: Generated imagery can alter how a real person appears to endorse or wear a product.

Mitigation: Use consented model references and avoid using the skill to fabricate unauthorized personal endorsements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline bash command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated JPEG image files through dLazy or another configured image provider.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
