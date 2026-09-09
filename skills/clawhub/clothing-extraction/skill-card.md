## Description:

Extracts clean e-commerce flat-lay product images from source fashion photos, removing people, props, and backgrounds while preserving the selected garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and e-commerce content teams use this skill to convert model, street-style, buyer-show, or competitor screenshots into clean garment flat-lay images for product listings and downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the selected image provider, creating data exposure for private or sensitive product imagery.

Mitigation: Use non-sensitive images or approved provider accounts, and confirm provider credentials and environment settings before running generation.

Risk: The helper scripts accept arbitrary image URLs and provider-returned URLs, which can create network exposure if internal or untrusted URLs are used.

Mitigation: Use trusted local image files or trusted public image URLs, avoid internal or private URLs, and review output URLs before downstream use.

Risk: Running a package through the npx path can introduce package provenance risk in sensitive environments.

Mitigation: Prefer a reviewed local installation or dry-run first, and only use npx where the package provenance is trusted.

Risk: Generated flat-lay images may infer occluded garment areas rather than faithfully recover hidden product details.

Mitigation: Manually review product-critical design areas and rerun with less-occluded source imagery when accuracy matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated assets are image files such as JPEG, PNG, or WebP.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default clothing-extraction generation uses gpt-image-2 at 1024x1024 with high quality; prompts and source images may be sent to the selected image provider.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
