## Description:

Transforms one product image and selling-point notes into a consistent ecommerce image set across multiple angles, scenes, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, marketers, and developers use this skill to turn one product or model reference image plus selling points into a set of product images for listing slots or detail pages while preserving visual identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference image URLs and prompts may be sent to external generation providers.

Mitigation: Use only non-sensitive product images and prompts, and review provider terms before use.

Risk: Arbitrary image URLs may be fetched by helper scripts.

Mitigation: Avoid internal, localhost, or private-network image URLs; use trusted public or local inputs.

Risk: Provider credentials may enable spend or access beyond the immediate task.

Mitigation: Use least-privilege API keys with spend limits and rotate or revoke keys when no longer needed.

Risk: Custom ARK_BASE_URL or npx CLI usage can execute or contact untrusted services.

Mitigation: Set ARK_BASE_URL only to a trusted HTTPS endpoint and treat the npx CLI path as executing code from npm.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated ecommerce images as JPEG, PNG, or WebP through the configured provider.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
