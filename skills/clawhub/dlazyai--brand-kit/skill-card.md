## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to define shared brand.yaml rules for model references, color, lighting, composition, whitespace, and copy tone, then apply them consistently across product image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images, including face references, are sent to the chosen cloud provider.

Mitigation: Choose the provider explicitly and confirm the inputs are suitable for upload before generating.

Risk: Image generation may incur charges.

Mitigation: Preview the request with --dry-run and review the selected task and provider before generating.

Risk: Provider credentials may be exposed if mishandled.

Mitigation: Protect provider keys and keep them out of prompts and shared files.

Risk: The external CLI and absent companion scripts are outside this release's security assessment.

Mitigation: Use a reviewed CLI version and check brand-file image paths before use.

## Reference(s):

- [Brand YAML schema](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Configuration files, Prompt text, Image files]

**Output Format:** [YAML brand configuration, text prompt additions, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files depend on the selected task and provider.]

## Skill Version(s):

1.0.27 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
