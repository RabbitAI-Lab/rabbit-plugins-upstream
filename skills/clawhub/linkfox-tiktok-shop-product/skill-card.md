## Description:

TikTok Shop ERP product-management skill for checking listing prerequisites, resolving shop ciphers, reading category, attribute, and brand data, and searching, creating, editing, listing, delisting, repricing, restocking, deleting, or recovering shop products through LinkFox's TikTok Shop product API gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and agents managing TikTok Shop ERP catalogs use this skill to inspect shop product state and perform catalog operations such as product creation, updates, activation, deactivation, price changes, inventory changes, deletion, and recovery. It depends on a separate LinkFox TikTok Shop auth skill for store selection and authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform catalog-changing TikTok Shop actions, including create, edit, activate, deactivate, price, inventory, delete, and recover operations.

Mitigation: Install only for agents and users authorized to manage the relevant TikTok Shop catalog, require confirmation for catalog-changing actions, and verify shop_cipher and product IDs before execution.

Risk: The product_proxy helper exposes raw developerProxy access for trusted TikTok Shop product and authorization paths.

Mitigation: Avoid product_proxy unless raw proxy access is intentionally needed in a trusted environment; prefer the named API helpers for routine workflows.

Risk: The security evidence verdict is suspicious because the skill has broad catalog-changing and proxy capabilities.

Mitigation: Review the skill before installation, restrict it to approved catalog-management contexts, and apply the server security guidance during deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-product)
- [LinkFox Skills](https://skill.linkfox.com/)
- [TikTok Shop ERP Product API Reference](artifact/references/api.md)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Partner Center: Check Listing Prerequisites](https://partner.tiktokshop.com/docv2/page/check-listing-prerequisites-202312)
- [TikTok Shop Partner Center: Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502)
- [TikTok Shop Partner Center: Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309)
- [TikTok Shop Partner Center: Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses from Python helper scripts, with concise Markdown or shell-command guidance when explaining workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include TikTok Shop API status, resolved paths, query strings, request bodies, shop_cipher values, and upstream response data; sensitive tokens should not be printed in full.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
