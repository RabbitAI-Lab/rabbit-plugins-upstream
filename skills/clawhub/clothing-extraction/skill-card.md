## Description:

从任意图提取干净商品平铺图。真人图 / 街拍图 → 白底平铺商品图。当用户说「提取衣服」「扒图」「转平铺」「抠成商品图」「从买家秀提取」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce creators, merchandisers, and developers use this skill to turn model photos, buyer photos, street shots, or competitor screenshots into clean flat-lay product images. It helps prepare square product assets or clean image inputs for related e-commerce image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to cloud image providers.

Mitigation: Use only images you are allowed to process and avoid submitting private or sensitive source material unless the selected provider is approved for that data.

Risk: Untrusted image URLs or loosely bounded provider settings could expose private network data or route data to an unintended endpoint.

Mitigation: Prefer local image files you control, avoid untrusted URLs, and set ARK_BASE_URL only to a trusted official or enterprise endpoint.

Risk: API keys may be exposed or misused if broad credentials are configured.

Mitigation: Use scoped provider API keys, store them in the provider's supported configuration or environment variables, and rotate or revoke keys when access is no longer needed.

Risk: The skill can infer occluded garment regions, which may produce inaccurate product details.

Mitigation: Review generated images against the source material, especially for blocked design areas, logos, fabric texture, color, seams, and symmetry.

Risk: Generated flat-lay images could be misused to remove branding or present another party's product as the user's own.

Mitigation: Use the skill only for authorized product work and do not use it to erase third-party branding or misrepresent product ownership.

## Reference(s):

- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Model Flags](artifact/references/model-flags.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and image file output paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent prepares prompts and commands for image generation; when executed, generated assets are saved as image files such as JPEG or PNG.]

## Skill Version(s):

1.0.6 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
