## Description:

亚马逊低价商品选品专家。适用于寻找或评估低价商品、价格带机会、平价细分市场、小额客单商品，以及按低售价过滤商品的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and sourcing teams use this skill to find low-price product opportunities across supported marketplaces, export Excel results, and optionally run ASIN scoring against their seller profile. It supports follow-up sorting, pagination, condition suggestions, and scheduled product scouting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can consume paid LinkFox or SellerSprite credits during product scouting, scoring, upload, and scheduling workflows.

Mitigation: Install and run it only in a controlled workspace, confirm cost-bearing actions before execution, and monitor credit usage for scheduled or repeated runs.

Risk: The security summary reports under-scoped abilities including recurring task creation, public upload/account/billing helpers, and environment-selected script execution.

Mitigation: Review the bundled helper skills before installation, remove unneeded scheduling or upload/account utilities, and avoid untrusted LINKFOX_TOOL_GATEWAY or SELLERSPRITE_SCRIPT environment settings.

Risk: The release includes utilities that can persistently rewrite other agents' instructions.

Mitigation: Quarantine or remove cross-agent patching utilities unless explicitly required, and review any agent instruction changes before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-low-price-product-expert)
- [Amazon product scout API parameter catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [SellerSprite product search API](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [ASIN dynamic scoring example expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File upload API](artifact/skills/linkfox-file-upload/references/api.md)
- [Report layout reference](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)
- [AIGC text generation API](artifact/skills/linkfox-aigc-textgen/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown conversation responses with shell commands, JSON snippets, Excel file paths, and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary product scouting and scoring results are expected as Excel exports with concise in-chat previews.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
