## Description:

Turns product details or online listings into ecommerce video ads with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing teams use this skill to turn product specifications, manuals, catalogs, or marketplace listings into shopping videos for ads and cross-border commerce.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to the third-party dLazy service.

Mitigation: Avoid sensitive prompts and attach only files needed for the video task.

Risk: Authentication can save an API key to local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: The skill depends on a third-party CLI package.

Mitigation: Review the linked CLI package and source before installing if supply-chain trust matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [CLI-streamed text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of ecommerce videos through the dLazy service; optional product files can be attached.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
