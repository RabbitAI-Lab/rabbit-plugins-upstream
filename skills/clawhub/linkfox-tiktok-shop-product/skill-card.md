## Description: <br>
Helps agents manage TikTok Shop ERP product catalogs, including shop lookup, listing readiness checks, categories, attributes, brands, product search, creation, edits, activation, deactivation, price and inventory updates, deletion, and recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to let an agent inspect and operate TikTok Shop ERP product listings after shop authorization is completed through the required auth skill. It supports catalog setup, listing validation, product maintenance, status changes, pricing, inventory, deletion, and recovery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live storefront data, including product creation, edits, activation, deactivation, price, inventory, deletion, and recovery. <br>
Mitigation: Require explicit user approval before mutating catalog actions and fetch current product data before edits. <br>
Risk: The generic product proxy can send broad allowed product or authorization requests beyond the named workflows. <br>
Mitigation: Prefer named scripts for normal use and use product_proxy.py only when the user has reviewed the target path, method, query, and body. <br>
Risk: Custom gateway environment variables can redirect calls to a different endpoint. <br>
Mitigation: Do not set custom gateway environment variables unless the endpoint is trusted and intended for this release. <br>
Risk: Shop identifiers, ciphers, request bodies, or responses may contain sensitive catalog or account data. <br>
Mitigation: Limit displayed sensitive values to what is needed for the task and avoid printing full access tokens or unnecessary account details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-product) <br>
- [TikTok Shop ERP Product API Reference](references/api.md) <br>
- [Get Authorized Shops](references/apis/get_authorized_shops.md) <br>
- [Check Listing Prerequisites](references/apis/check_listing_prerequisites.md) <br>
- [Get Categories](references/apis/get_categories.md) <br>
- [Get Category Rules](references/apis/get_category_rules.md) <br>
- [Get Attributes](references/apis/get_attributes.md) <br>
- [Recommend Category](references/apis/recommend_category.md) <br>
- [Get Brands](references/apis/get_brands.md) <br>
- [Search Products](references/apis/search_products.md) <br>
- [Get Product](references/apis/get_product.md) <br>
- [Create Product](references/apis/create_product.md) <br>
- [Edit Product](references/apis/edit_product.md) <br>
- [Partial Edit Product](references/apis/partial_edit_product.md) <br>
- [Check Product Listing](references/apis/check_product_listing.md) <br>
- [Activate Product](references/apis/activate_product.md) <br>
- [Deactivate Products](references/apis/deactivate_products.md) <br>
- [Update Price](references/apis/update_price.md) <br>
- [Update Inventory](references/apis/update_inventory.md) <br>
- [Delete Products](references/apis/delete_products.md) <br>
- [Recover Products](references/apis/recover_products.md) <br>
- [TikTok Shop Partner Center: Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) <br>
- [TikTok Shop Partner Center: Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) <br>
- [TikTok Shop Partner Center: Update Inventory](https://partner.tiktokshop.com/docv2/page/update-inventory-202309) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request or response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call live TikTok Shop ERP product APIs through LinkFox scripts and return upstream status, parsed body data, resolved paths, query strings, and request bodies.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
