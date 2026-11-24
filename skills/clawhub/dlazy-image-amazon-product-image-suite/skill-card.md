## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform. Outputs comply with Amazon's image guidelines while optimizing for click-through and conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and their creative teams use this skill to plan and produce compliant product detail-page imagery and A+ content. It guides image planning, prompts, and dLazy CLI use for main, secondary, and brand-content images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an unexplained dLazy login step and a Chinese-only confirmation flow; its analysis was partial because local references were unresolved.

Mitigation: Review the CLI login flow and unresolved references before authenticating. Use a revocable API key and rotate it if needed.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Generated image assets and URLs, with Markdown plans and checklists, image prompts, and CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation uses the dLazy service; supplied local media may be uploaded for processing.]

## Skill Version(s):

1.3.44 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
