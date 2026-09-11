## Description:

生成带中文排版的详情页模块，将商品图和卖点转化为可上架的电商详情页图文模块。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agents use this skill to generate Chinese-layout product detail page modules from product images and short selling points. It focuses on banners, selling-point icon rows, material blocks, detail blocks, and parameter sections while preserving product appearance and avoiding unsupported claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and generated outputs may be processed by dLazy or the selected cloud provider.

Mitigation: Use non-sensitive product assets, review provider data handling before use, and avoid submitting confidential images or private commercial data.

Risk: Untrusted image URLs or private-network URLs may be fetched during generation.

Mitigation: Use trusted local files or public asset URLs only, and do not pass metadata-service, intranet, or other sensitive URLs as inputs.

Risk: A configurable Ark endpoint can receive the Ark API key and user assets.

Mitigation: Set ARK_BASE_URL only to a trusted endpoint and prefer dry-run or explicit provider selection before transmitting assets or spending credits.

Risk: Generated ecommerce copy may introduce unsupported product claims or inaccurate rendered text.

Mitigation: Keep selling points grounded in supplied product information, check generated Chinese text character by character, and remove unsupported promotions, certifications, or comparison claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and optional generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are typically saved as JPG files at user-selected paths; dry-run mode can preview requests and estimated credits before execution.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
