## Description:

Helps ecommerce sellers connect a shop, find 1688 products from images, and preview or publish selected products through the production 小天铺货 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daiyangyang103240](https://clawhub.ai/user/daiyangyang103240)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers use this assistant to connect their shop, check authorization, find similar or lower-priced 1688 products from images, and preview or publish selected listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a shop stores a local session token for the production service.

Mitigation: Connect only an intended shop; keep the local session private and never include the token in user-facing results.

Risk: Product images or links are sent to the production service for sourcing and preview.

Mitigation: Submit only product material you intend to share with the service and review sourced results before choosing products.

Risk: Publishing can create live product listings.

Mitigation: Review the preview and confirm before publishing, or explicitly request automatic publishing; stop blocked items rather than guessing required attributes.

## Reference(s):

- [Agent protocol](references/api-protocol.md)
- [小天铺货 service](https://puhuo.huitun.com)
- [ClawHub skill listing](https://clawhub.ai/daiyangyang103240/skills/xtph-ecommerce-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Chinese text and Markdown product tables with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes shop status, sourcing results, preview blockers, publication outcomes, and links for manual follow-up; excludes session tokens and raw product drafts.]

## Skill Version(s):

1.0.14 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
