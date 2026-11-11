## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams use this skill to define a reusable brand.yaml for consistent product imagery across SKUs, including model, lighting, composition, and visual tone. Agents can apply the relevant brand rules when preparing image-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete: some generation and provider-authentication scripts were only partially inspected, and the scan flags capabilities beyond the stated brand-configuration purpose.

Mitigation: Review generation and provider-authentication behavior before installation.

Risk: Prompts and reference images may be sent to the selected external generation provider.

Mitigation: Confirm the selected provider and its data handling before sending prompts or images.

Risk: Provider credentials are required and their storage method should be checked.

Mitigation: Review how credentials are stored and use credentials that can be rotated or revoked.

## Reference(s):

- [Brand configuration schema](references/brand-schema.md)
- [Provider and generation usage guide](references/provider-cli.md)
- [Ecommerce skills source repository](https://github.com/dlazy-ai/ecommerce-skills)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Configuration, Prompt guidance, Shell commands]

**Output Format:** [YAML configuration and Markdown instructions with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reusable brand rules are applied selectively to supported image tasks.]

## Skill Version(s):

1.0.29 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
