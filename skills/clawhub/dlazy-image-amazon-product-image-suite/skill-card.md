## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform. Outputs comply with Amazon's image guidelines while optimizing for click-through and conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers, e-commerce designers, and agents use this skill to plan and generate Amazon product-detail imagery, including compliant main images, secondary infographics, lifestyle/detail shots, and A+ Brand Content modules through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media may be sent to dLazy cloud endpoints.

Mitigation: Avoid uploading sensitive product files unless intended, and review data handling before use.

Risk: Global CLI installation can leave a persistent local API key and a third-party CLI on the user's system.

Mitigation: Prefer npx or review the CLI source before global installation, and use a revocable API key or DLAZY_API_KEY for per-run credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with command snippets, checklists, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy-hosted image result URLs; image generation is performed by the third-party CLI/API.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
