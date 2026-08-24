## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform, covering main images, secondary images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, brand teams, and commerce operators use this skill to plan and generate product-detail visual assets through the dLazy CLI. It supports main-image baselines, secondary product images, lifestyle or infographic assets, and A+ page modules while maintaining image consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and provided media are sent to dLazy services for generation.

Mitigation: Review prompt content and media before confirming generation commands, and use the service only when cloud processing is acceptable.

Risk: The login flow can persist an API key in the local dLazy CLI configuration file.

Mitigation: Use DLAZY_API_KEY for per-command authentication when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: The workflow depends on an external CLI and hosted API endpoints.

Mitigation: Review the pinned @dlazy/cli package before installation and confirm each generated command before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown status updates with prompt drafts, CLI command proposals, image checklists, and generated result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before each image generation command and uses pinned @dlazy/cli installation guidance.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
