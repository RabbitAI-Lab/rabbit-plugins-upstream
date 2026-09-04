## Description:

Routes 1688 order-inquiry tasks for sending merchant questions, querying replies, and configuring inquiry dialogue, and extracts Shopify or AliExpress SKU variants as JSON records with image and query fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and supply-chain agents use this skill to ask merchants about existing 1688 orders, check inquiry responses, configure inquiry dialogue behavior, and extract SKU variant image/query data from Shopify or AliExpress product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send merchant inquiries or change inquiry dialogue settings for specified 1688 orders.

Mitigation: Use it only with order IDs, questions, attachments, and settings that the operator explicitly intends to submit.

Risk: The skill requires access to a 1688 AK and may store or read that credential for signed requests.

Mitigation: Limit AK access to trusted environments, rotate exposed keys, and verify the configured key source before running order actions.

Risk: The security review notes signed usage telemetry and automatic dependency repair at runtime.

Mitigation: Review the telemetry behavior and dependency installation path before deployment in controlled or restricted environments.

Risk: Local attachment paths can be read and uploaded when included in an inquiry request.

Mitigation: Provide only attachment paths that are intended for merchant inquiry use and avoid sensitive local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-supplychain-order-inquiry)
- [AK configuration capability](references/capabilities/configure.md)
- [Inquiry configuration capability](references/capabilities/inquiry_config.md)
- [Inquiry query capability](references/capabilities/inquiry_query.md)
- [Inquiry send capability](references/capabilities/inquiry_send.md)
- [AliExpress SKU extraction capability](references/capabilities/sku_extract_aliexpress.md)
- [Shopify SKU extraction capability](references/capabilities/sku_extract_shopify.md)
- [Structured parameters reference](references/capabilities/structured-params.md)
- [Error handling reference](references/common/error-handling.md)
- [Usage telemetry reference](references/skill埋点说明.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Pure JSON object or JSON array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inquiry outputs include task identifiers, status, summaries, or configuration state; SKU extraction outputs arrays of image/query records and omits price, inventory, and store data.]

## Skill Version(s):

0.57.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
