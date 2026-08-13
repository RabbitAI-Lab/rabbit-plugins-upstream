## Description:

基于卖家精灵的亚马逊潜力单变体选品专家。适用于寻找变体结构简单、变体复杂度低、具备销量或增长信号、开发路径更清晰的单变体商品机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product researchers use this skill to find simple single-variation product opportunities with recent growth signals across supported Amazon marketplaces. It filters SellerSprite product data, exports scouting results to Excel, and can run profile-based ASIN scoring for deeper prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package can use LinkFox credentials and includes account, phone/SMS registration, and paid plan ordering flows.

Mitigation: Install only after verifying the publisher, endpoints, and account flow; use scoped credentials and avoid entering payment, phone, or API-key details unless those flows are intended.

Risk: The package can upload local files to public URLs.

Mitigation: Review files before upload and avoid sending private, regulated, or customer data through the upload capability.

Risk: The package can create scheduled tasks that repeatedly execute prompts or workflows.

Mitigation: Confirm task frequency, cost, notification targets, and task status before enabling automation.

Risk: The package contains a utility that can rewrite other agents' instruction files.

Mitigation: Review and approve any instruction-file changes before use, and keep backups or version control for affected agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-single-variation-potential-scout)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [SellerSprite product search API reference](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [Amazon product scout API parameters catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [Dynamic scoring example expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [Task scheduler API reference](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown responses with tables, JSON status blocks, shell commands, and Excel file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Excel workbooks for scouting and scoring results; may include local file paths, API cost summaries, and next-step prompts.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
