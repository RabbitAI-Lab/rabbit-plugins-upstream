## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform, including main images, secondary images, and A+ content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and commerce teams use this skill to plan and generate Amazon product image suites, including compliant main images, secondary product visuals, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy cloud services.

Mitigation: Confirm prompts and file paths before each command, and avoid using sensitive or unauthorized media.

Risk: The dLazy API key may be stored locally or supplied through the environment.

Mitigation: Use the documented login or DLAZY_API_KEY flow, protect local configuration files, and rotate or revoke keys when needed.

Risk: Generated product images may include inaccurate claims, misleading visuals, or marketplace compliance issues.

Mitigation: Review generated assets against the source product, Amazon image requirements, and approved product claims before publication.

Risk: A long-lived global npm CLI install may not fit all environments.

Mitigation: Prefer the documented npx option when a temporary pinned invocation is more appropriate than a global install.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status updates with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke dLazy CLI commands that send prompts and selected local media to dLazy cloud services.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
