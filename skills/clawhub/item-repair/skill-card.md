## Description:

Retouches casual product photos into listing-ready images by reducing random wrinkles, straightening layout, evening lighting, and cleaning backgrounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and content teams use this skill to guide agents in retouching single-product images for online listings while preserving product color, style, structure, labels, and intentional folds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive product images or paid provider keys may be exposed if the skill is installed or executed in an untrusted environment.

Mitigation: Review before installing, use dry-run first, prefer the documented dLazy/default provider, and avoid custom ARK_BASE_URL endpoints unless they are fully trusted.

Risk: The bundled generator has broader provider and URL-handling authority than the product-photo retouching task clearly requires.

Mitigation: Review commands and provider settings before execution, and scan the skill before deployment.

Risk: The optional npx CLI path can execute a third-party package.

Mitigation: Use that path only when third-party package execution is acceptable for the deployment environment.

## Reference(s):

- [Model flags](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Related material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, inline shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may save generated image files when executed with a configured provider.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
