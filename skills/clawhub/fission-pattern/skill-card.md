## Description:

根据一张商品参考图和卖点，生成多角度、多场景的电商商品套图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家和设计人员可将单张商品图与产品卖点扩展为统一风格的主图、场景图和细节图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chosen product images, prompts, and optional brand references are sent to the selected cloud image provider.

Mitigation: Use only images and brand materials you are comfortable sharing with that provider.

Risk: Available provider credentials may determine which service receives generation requests.

Mitigation: Review configured credentials and use --dry-run to inspect the request before generation.

Risk: Generated images may be saved to unintended locations or differ from the reference product.

Mitigation: Choose --save paths deliberately and review the complete image set for product accuracy before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a coordinated set of five product images saved to user-chosen paths.]

## Skill Version(s):

1.0.14 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
