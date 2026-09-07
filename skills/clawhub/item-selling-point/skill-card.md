## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。当用户说「主图」「加卖点文案」「转化图」「促销图」「主图文案」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and developers use this skill to turn one product image plus selling-point copy into a square or vertical main listing image with concise Chinese promotional text and layout guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and credentials may be sent to the selected generation provider, and the ARK provider path can use an environment-defined base URL.

Mitigation: Use the default dLazy provider or another verified provider configuration, avoid untrusted ARK_BASE_URL and DLAZY_BIN values, and run dry-run first when checking requests.

Risk: Generated listing images may contain unsupported product claims, false promotions, absolute advertising language, unreadable Chinese text, or unintended changes to product appearance.

Mitigation: Verify product claims and promotions before generation, keep copy short, inspect the output at thumbnail size, and confirm the generated image preserves product shape, color, material, and logos.

Risk: A bundled remove-watermark task exists in shared task configuration and may be misused on images without proper rights.

Mitigation: Do not use watermark-removal behavior unless the user owns the image rights and has a legitimate restoration need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands that generate image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are saved to local image paths; dry-run mode can preview requests and estimated credits before calling a provider.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
