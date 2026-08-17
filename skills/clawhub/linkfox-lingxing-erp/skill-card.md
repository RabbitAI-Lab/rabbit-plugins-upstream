## Description:

This LinkFox skill helps agents query Lingxing ERP OpenAPI data across advertising, sales, products, finance, inventory, FBA, purchasing, customer service, and multi-platform operations using Lingxing credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce operators use this skill to prepare and run Lingxing ERP OpenAPI queries for operational reporting and analysis across ads, orders, listings, inventory, finance, FBA, purchasing, service, and multi-platform datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags under-disclosed LinkFox login, API-key, and payment flows in addition to Lingxing ERP querying.

Mitigation: Install only when LinkFox is intentionally trusted, and review the LinkFox onboarding and billing scripts before using any SMS, API-key, plan, or payment workflow.

Risk: The skill can persist Lingxing tokens, QR/payment files, and large ERP responses locally.

Mitigation: Keep generated files outside source repositories, remove cached tokens, QR files, and persisted ERP response files after use, and avoid committing output that may contain PII, pricing, or credential-sensitive data.

Risk: Endpoint override environment variables and API credentials affect where requests are sent and what account data can be accessed.

Mitigation: Control endpoint override environment variables, scope Lingxing credentials to the minimum needed permissions, and follow Lingxing IP allowlist and credential-rotation practices.

## Reference(s):

- [Lingxing OpenAPI host](https://openapi.lingxing.com)
- [API usage overview](references/api.md)
- [Product APIs](references/product.md)
- [Advertising base data APIs](references/basedata.md)
- [Advertising report APIs](references/newad-report.md)
- [Sales operations APIs](references/sale-ops.md)
- [Full sales APIs](references/sale-full.md)
- [Finance APIs](references/finance.md)
- [Statistics APIs](references/statistics.md)
- [FBA APIs](references/fba.md)
- [Amazon source data APIs](references/sourcedata.md)
- [Warehouse APIs](references/warehouse.md)
- [Customer service APIs](references/service.md)
- [Onboarding and billing flow notes](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist large ERP responses to local files for later field extraction; persisted files may contain sensitive business data and are not automatically deleted.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
