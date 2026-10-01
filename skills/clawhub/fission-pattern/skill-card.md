## Description:

将一张商品参考图和卖点扩展为多角度、多场景的电商商品套图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商卖家及内容制作人员，根据商品参考图和卖点制作同一商品的主图、场景图及细节图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and provider credentials are sent to the configured image-generation service.

Mitigation: Use only a provider you trust and submit only images, prompts, and credentials you are comfortable sharing.

Risk: Using unlicensed images or removing watermarks may infringe others' rights.

Mitigation: Use assets you own or are licensed to modify, particularly before removing a watermark.

Risk: Generated files may overwrite existing outputs if paths conflict.

Mitigation: Choose distinct output paths for each generated image.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [Model options reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown with shell examples; generated JPEG images when commands are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a coordinated set of product views at user-selected output paths.]

## Skill Version(s):

1.0.15 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
