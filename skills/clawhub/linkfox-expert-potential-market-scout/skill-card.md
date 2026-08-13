## Description:

Amazon potential-market product scouting expert for finding moderate-volume growth products, emerging market opportunities, recently listed products, sortable scouting runs, scheduled scouting, and Excel exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and e-commerce analysts use this skill to identify products with monthly sales at or below 600 units, at least 10% month-over-month sales growth, and recent listing dates. The skill can preview results, export Excel workbooks, continue across pages without duplicates, schedule recurring scouting, and optionally score candidate ASINs against seller preferences.

### Deployment Geography for Use:

Global; documented Amazon marketplace support covers US, UK, DE, FR, JP, CA, IT, ES, MX, and IN.

## Known Risks and Mitigations:

Risk: The package includes capabilities beyond Amazon market scouting, including account/payment onboarding, public file upload, AI text generation, task deletion, and agent-modification utilities.

Mitigation: Review the package before installation, use it only in a trusted environment, and invoke those broader utilities only when they are explicitly needed.

Risk: The skill can use LINKFOX_* credentials and produce sensitive artifacts such as API keys, phone numbers, payment order data, webhook URLs, raw result files, and uploaded-file URLs.

Mitigation: Control LINKFOX_* environment variables and treat generated keys, webhook URLs, raw files, and uploaded URLs as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-potential-market-scout)
- [Amazon product scout API parameters](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [SellerSprite product search API](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [ASIN scoring expectations example](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown conversation output with command guidance, tabular previews, JSON/script outputs, and Excel workbook file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary product and scoring deliverables are Excel files; conversation output includes concise previews, status, sorting guidance, and full local file paths.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
