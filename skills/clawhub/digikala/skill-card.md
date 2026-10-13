## Description:

Helps Digikala sellers use the Marketplace Open API to find categories and products, upload images, and manage product listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Digikala sellers and developers use this skill to search products and categories, validate listings, upload images, and create or assign products through the seller API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using the seller API token can access the seller account within its granted permissions.

Mitigation: Provide the token through an environment variable where possible, grant minimal scopes, and protect any token file.

Risk: Product creation, assignment, title changes, and image uploads can affect live marketplace data.

Mitigation: Review product details and image payloads before write commands, confirm state-changing actions, and test workflows in the sandbox first.

## Reference(s):

- [Source repository (server-resolved)](https://github.com/ehsanghaffar/skills/tree/main/skills/digikala)
- [Digikala Marketplace API](https://seller.digikala.com/open-api/v1/)
- [API endpoint reference](artifact/references/endpoints.md)
- [Seller API sandbox](https://github.com/salimousavi/seller_service_sandbox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the seller's API token, permissions, and live marketplace data.]

## Skill Version(s):

0.1.3 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
