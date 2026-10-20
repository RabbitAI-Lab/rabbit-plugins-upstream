## Description:

Helps create e-commerce outfit photos combining up to eight product images on one model while aiming to preserve each item's details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Retailers, creative teams, and their agents can prepare prompts and generation commands to combine product photos into coordinated model-worn looks for e-commerce listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product or model images may be sent to the selected cloud provider.

Mitigation: Choose the provider deliberately and submit private, personal, or proprietary images only with permission and acceptance of its data handling.

Risk: Cloud generation may consume paid credits, and the generated look may omit or alter product details.

Mitigation: Preview the request and estimated cost with dry-run before generation; inspect outputs against the supplied product images before publishing.

## Reference(s):

- [ClawHub image-fusion release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI and data-flow reference](artifact/references/provider-cli.md)
- [Image model parameters](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with generation prompts and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated outfit images to a chosen file path; review the results for product fidelity.]

## Skill Version(s):

1.0.24 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
