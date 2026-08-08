## Description:

Provides agent guidance and scripts for working with authorized Shopee store orders through LinkFox's Shopee developer proxy, including order lookup, package and shipment queries, cancellations, notes, booking workflows, and invoice/FBS operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to retrieve and manage Shopee order data for authorized stores, including order lists and details, package and shipment views, cancellations, buyer-cancellation handling, notes, and invoice/FBS workflows.

### Deployment Geography for Use:

Global, subject to Shopee API regional restrictions noted for invoice and FBS endpoints.

## Known Risks and Mitigations:

Risk: The skill can perform live Shopee order-changing actions such as cancellation, split or unsplit, buyer-cancellation handling, invoice upload, note updates, payment onboarding, and prescription-related actions.

Mitigation: Require explicit human confirmation before executing any action that changes orders, uploads documents, starts payment flows, or affects account state.

Risk: Full order responses may be stored locally and can include sensitive order or customer data.

Mitigation: Review and regularly delete the local linkfox output directory, avoid sharing saved response files, and restrict workspace access.

Risk: The skill depends on a local LinkFox API key for account and Shopee store access.

Mitigation: Store the API key only in environment variables, avoid pasting it into prompts or files, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-orders)
- [Shopee Open Platform Order Module](https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1)
- [LinkFox Shopee Orders API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown guidance with Python shell commands and JSON request/response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full responses to local linkfox/<date>/<session>/data JSON files and may print summaries for large responses.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
