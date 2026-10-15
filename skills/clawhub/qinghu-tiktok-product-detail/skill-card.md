## Description:

Looks up details for up to 10 TikTok Shop products per request using Qinghu AI's product-detail tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to retrieve TikTok Shop product details, including prices and sales data, for specified product IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-led installation or updates of Node and qhkit can change the local runtime and persistent PATH settings.

Mitigation: Preinstall a reviewed qhkit version yourself and require explicit approval before any local runtime installation or update.

Risk: Configuring the Qinghu API token may expose or persist a service credential.

Mitigation: Use a session-scoped token or environment variable and avoid persisting credentials unnecessarily.

Risk: Product-detail requests incur Qinghu credits, with charges varying by returned result volume.

Mitigation: Check the current estimate and obtain explicit approval before each planned paid batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise findings with product data; large result sets may be delivered as JSON or table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 10 product IDs per request; paid calls use Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
