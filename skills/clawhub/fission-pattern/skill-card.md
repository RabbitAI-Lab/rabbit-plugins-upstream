## Description:

Turns one product photo and its selling points into a coordinated set of ecommerce product images across angles and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use the skill to plan and generate consistent product-image sets from a reference photo for listings and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are uploaded to the selected cloud image provider.

Mitigation: Avoid confidential unreleased products or personal images unless the provider is approved by your organization.

Risk: Cloud image-generation requests may incur charges and require provider API keys.

Mitigation: Use --dry-run to review requests and estimated costs; keep API keys scoped and revocable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executed commands can save generated product-image files.]

## Skill Version(s):

1.0.19 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
