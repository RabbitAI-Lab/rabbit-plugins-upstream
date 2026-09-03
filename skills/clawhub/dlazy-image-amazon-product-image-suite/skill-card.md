## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform, covering main product images, secondary images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace teams, and e-commerce content operators use this skill to plan and generate Amazon-ready product image sets, including main images, secondary detail-page images, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media files are sent to dLazy hosted services for processing.

Mitigation: Use the skill only with assets approved for external SaaS processing, and avoid uploading sensitive product, customer, or unreleased brand material unless that use is authorized.

Risk: The workflow requires a dLazy API key, which may be stored in a local CLI configuration file or supplied by environment variable.

Mitigation: Protect the local configuration file, prefer organization-approved credential handling, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Package version evidence is inconsistent: install metadata points to @dlazy/cli 1.2.3 while artifact prose mentions 1.0.9.

Mitigation: Confirm the intended @dlazy/cli version before installation and use a pinned install or npx command that matches the approved release metadata.

Risk: Generated marketplace images can be inaccurate or noncompliant if product details, claims, or Amazon image requirements are not reviewed.

Mitigation: Review each generated image against product facts, brand requirements, and Amazon image rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sequential workflow that asks for confirmation before each image generation step; generated results are returned as hosted media URLs when the dLazy CLI call succeeds.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
