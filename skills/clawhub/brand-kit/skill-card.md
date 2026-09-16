## Description:

Brand Kit helps agents apply a shared brand.yaml visual standard for ecommerce image generation so product SKUs keep consistent models, lighting, composition, spacing, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators and agents use this skill to create and reuse a brand.yaml standard that appends consistent visual constraints and reference images to product image-generation tasks. It is intended for store-scale visual consistency across many SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed cloud image-generation providers may be selected from environment keys or local provider configuration.

Mitigation: Review provider credentials before use, run the doctor or dry-run mode first, and install only when cloud generation is intended.

Risk: Untrusted image URLs or reference images may be fetched and sent to a configured provider.

Mitigation: Use trusted local image assets or trusted URLs, and review all image inputs before running generation.

Risk: The default brand template includes model demographic fields that may not match the user's brand requirements.

Mitigation: Replace or remove the default model description and reference image before applying the brand file to production SKUs.

Risk: A custom Ark base URL can redirect requests to an endpoint outside the expected provider path.

Mitigation: Use ARK_BASE_URL only for endpoints the user fully trusts and controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml field reference](artifact/references/brand-schema.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with YAML configuration examples and Node.js shell commands; helper scripts can emit JSON dry-run or generation envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can append brand constraints to prompts, add a model reference image when available, run dry-runs, and save generated image or video files through configured cloud providers.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
