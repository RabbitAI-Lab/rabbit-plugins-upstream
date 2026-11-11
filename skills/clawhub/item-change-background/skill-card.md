## Description:

商品换背景。白底商品图 → 逼真场景图，光影与投影匹配新环境。当用户说「换背景」「加场景」「白底转场景」「放到桌面上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and product-content teams use this skill to turn isolated product photos into realistic lifestyle scenes while matching perspective, lighting, contact shadows, and reflections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts may be sent to an external image provider for processing.

Mitigation: Before use, check which provider will receive the images and prompts and whether it is approved for the data.

Risk: The security review reports incomplete inspection and undeclared tool scope.

Mitigation: Review the skill files and requested tool access before installation, and avoid sending sensitive inputs until the scope is understood.

Risk: The documented command-line reference is not version-pinned.

Mitigation: Verify the command source and version before running it.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [Related clothing extraction skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-extraction/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated image files (JPEG by default) with image-editing prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a product image and optionally a background image; output is saved to a user-specified path.]

## Skill Version(s):

1.0.31 (source: frontmatter; release evidence confirms version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
