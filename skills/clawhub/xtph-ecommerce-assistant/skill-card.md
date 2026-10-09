## Description:

Helps ecommerce sellers connect shops, find 1688 products from images, and preview or publish product listings through a production service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daiyangyang103240](https://clawhub.ai/user/daiyangyang103240)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers use this skill to connect a shop, check authorization, find 1688 sources from product images, and preview or publish selected listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, selected 1688 links, and shop workflow data are sent to the production service.

Mitigation: Connect a shop only when you intend to use this service, and share only the product inputs needed for the task.

Risk: A shop session token is stored locally after authorization.

Mitigation: Protect local session files and do not disclose session tokens.

Risk: Automatic publishing can submit ready listings without a separate confirmation step.

Mitigation: Review listing previews and use confirmation-based publishing unless you explicitly want automatic submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/daiyangyang103240/skills/xtph-ecommerce-assistant)
- [Production service](https://puhuo.huitun.com)
- [API protocol reference](artifact/references/api-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Chinese text and Markdown product tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image-search results show up to 10 products with full 1688 links.]

## Skill Version(s):

1.0.15 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
