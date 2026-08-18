## Description:

Helps agents manage Shopee cross-border GlobalProduct catalogs through LinkFox scripts for category lookup, global item and SKU management, publishing, pricing, stock, size charts, and related API tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage authorized Shopee cross-border global products, including category discovery, global item creation and updates, SKU operations, publishing to local shops, price and stock changes, and size-chart workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live Shopee store changes, including delete, publish, price, stock, and sync actions.

Mitigation: Require explicit human confirmation before running any operation that changes live store data.

Risk: The skill uses API keys, login-related flows, billing state, and local response logging that may expose sensitive business data.

Mitigation: Run it in an isolated workspace with trusted environment variables, do not share credentials or OTP output in logs, and clean up the local linkfox output directory when it is no longer needed.

Risk: Endpoint environment variables can alter where requests are sent.

Mitigation: Verify LinkFox endpoint variables before use and avoid running the skill when those variables are supplied by an untrusted environment.

## Reference(s):

- [Skill source overview](artifact/SKILL.md)
- [GlobalProduct API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Shopee GlobalProduct official documentation](https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1)
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-global-product)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are summarized for large payloads, and complete responses are written under a local linkfox output directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
