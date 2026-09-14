## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and developers use this skill to turn product images and short selling points into Chinese item-detail image modules for storefront listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and brand assets may be sent to external generation providers.

Mitigation: Use only product assets that are approved for external processing, avoid private or sensitive inputs, and choose a trusted configured provider before running generation commands.

Risk: The tool can fetch image inputs and generated outputs from URLs.

Mitigation: Prefer local image files or trusted HTTPS image hosts, and avoid private or internal URLs.

Risk: Ark API keys can be sent to a configurable endpoint.

Mitigation: Use ARK_BASE_URL only with endpoints you fully trust, or leave it unset to use the documented default endpoint.

Risk: Generated Chinese text or ecommerce claims may be wrong or misleading.

Mitigation: Review generated text, product fidelity, and claims before publishing, and do not add unsupported certifications, promotions, or comparison data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated ecommerce detail images locally; some commands can emit JSON status and file paths.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
