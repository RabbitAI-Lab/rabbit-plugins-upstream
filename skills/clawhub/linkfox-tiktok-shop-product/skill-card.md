## Description:

TikTok Shop ERP product-management skill that helps agents use LinkFox forwarding scripts for product prerequisites, shop cipher lookup, categories, attributes, brands, product search, create and edit workflows, listing checks, activation and deactivation, price and inventory updates, deletion, and recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage TikTok Shop ERP catalog data through named product API scripts after completing LinkFox TikTok Shop authorization. It supports product discovery, listing preparation, catalog creation and edits, status changes, and price or inventory maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live changes to TikTok Shop catalog data, including create, edit, delete, activate or deactivate, price, and inventory operations.

Mitigation: Require an exact before-and-after summary and explicit user confirmation before running any mutating command.

Risk: The generic product_proxy.py path can be easier to misuse than the named scripts.

Mitigation: Prefer the named scripts for supported APIs and reserve product_proxy.py for reviewed cases where the target path, method, query, and body are clear.

Risk: Changing LINKFOX_TOOL_GATEWAY or TIKTOK_SHOP_API_BASE_URL can route requests through an unintended gateway.

Mitigation: Keep those environment variables unset unless intentionally using a trusted LinkFox-compatible gateway.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-product)
- [TikTok Shop ERP Product API Reference](references/api.md)
- [TikTok Shop Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Check Listing Prerequisites](https://partner.tiktokshop.com/docv2/page/check-listing-prerequisites-202312)
- [TikTok Shop Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502)
- [TikTok Shop Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309)
- [TikTok Shop Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309)
- [TikTok Shop Update Inventory](https://partner.tiktokshop.com/docv2/page/update-inventory-202309)
- [TikTok Shop Update Price](https://partner.tiktokshop.com/docv2/page/update-price-202309)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized TikTok Shop ERP openId; most product APIs also require or resolve a shop_cipher.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
