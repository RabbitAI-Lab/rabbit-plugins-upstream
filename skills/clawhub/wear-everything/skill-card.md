## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 -> 真人佩戴图，落位、透视与阴影自然。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, creators, and developers use this skill to generate on-model product imagery for shoes, bags, jewelry, eyewear, watches, hats, scarves, and similar accessories while preserving the product appearance and reference model context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images are sent to the selected image-generation provider.

Mitigation: Use only approved product and model assets, review provider selection before execution, and run dry-run first when checking requests or cost.

Risk: Untrusted image URLs may point to localhost, private networks, or cloud metadata services.

Mitigation: Prefer trusted local files or vetted public image URLs, and reject private-network or metadata-service URLs before running generation.

Risk: An overridden Ark endpoint can receive Ark credentials.

Mitigation: Inspect PROVIDER and ARK_BASE_URL before execution, use scoped and revocable API keys, and route credentials only to trusted gateways.

Risk: Bundled shared helper tasks include watermark-removal behavior outside the normal wear-everything workflow.

Mitigation: Use any watermark-removal task only for images where removal is legitimate and rights are owned or authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, provider configuration notes, and generated image files when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, batch generation, brand prompt additions, and provider selection through documented environment variables.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
