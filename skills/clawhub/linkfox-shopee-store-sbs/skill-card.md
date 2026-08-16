## Description:

Shopee-店铺SBS lets agents query authorized Shopee SBS warehouse and inventory data through LinkFox wrappers for the five Shopee SBS endpoints: bound warehouses, current inventory, expiry reports, stock aging, and stock movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, store operators, and their agents use this skill to inspect SBS warehouse binding, current inventory, expiry, stock aging, and stock movement data for authorized stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Shopee store data through LinkFox gateway services and can handle phone/SMS login, API-key provisioning, and billing-related flows.

Mitigation: Install and run it only when LinkFox handling those data and account flows is acceptable for the deployment.

Risk: Generated API keys and saved response files can contain sensitive account or store information.

Mitigation: Treat API keys and local linkfox session data as sensitive, restrict access to the workspace, and delete saved response files when they are no longer needed.

Risk: Environment overrides can redirect service URLs.

Mitigation: Use service URL override environment variables only for endpoints controlled by the operator.

Risk: Onboarding actions can create payment orders or expose payment QR data.

Mitigation: Confirm user intent before running billing commands and show the returned payment details for user review.

## Reference(s):

- [SBS module API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee get_bound_whs_info documentation](https://open.shopee.com/documents/v2/v2.sbs.get_bound_whs_info?module=124&type=1)
- [Shopee get_current_inventory documentation](https://open.shopee.com/documents/v2/v2.sbs.get_current_inventory?module=124&type=1)
- [Shopee get_expiry_report documentation](https://open.shopee.com/documents/v2/v2.sbs.get_expiry_report?module=124&type=1)
- [Shopee get_stock_aging documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_aging?module=124&type=1)
- [Shopee get_stock_movement documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_movement?module=124&type=1)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses saved to local files and printed or summarized on stdout, with Markdown guidance and shell commands for setup or recovery flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized on stdout unless --inline is used; full responses are saved under linkfox/<date>/<session>/data/.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
