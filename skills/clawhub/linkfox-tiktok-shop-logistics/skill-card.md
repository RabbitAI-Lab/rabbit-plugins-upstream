## Description:

Helps agents retrieve authorized TikTok Shop shops and warehouse lists for ERP logistics workflows using a configured LinkFox account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to look up TikTok Shop warehouse identifiers and shop ciphers before product listing, inventory, or multi-warehouse workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes generic proxy scripts that can call broader authenticated logistics and authorization paths than a warehouse-list-only reader may expect.

Mitigation: Install only if that broader access is intentional, or prefer a version that removes the generic proxy and allowlists only the documented warehouse endpoint.

Risk: The skill uses a configured API key and ERP openId to access seller shop and warehouse data through LinkFox.

Mitigation: Limit execution to trusted environments, avoid exposing tokens or full credentials in outputs, and review the requested path before running proxy commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-logistics)
- [TikTok Shop ERP Logistics API Reference](references/api.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [Get Warehouse List](references/apis/get_warehouse_list.md)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Partner Center: Get Warehouse List](https://partner.tiktokshop.com/docv2/page/get-warehouse-list-202309)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured LinkFox API key and an ERP openId from linkfox-tiktok-shop-auth.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
