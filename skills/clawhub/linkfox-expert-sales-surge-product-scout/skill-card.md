## Description:

亚马逊销量飙升榜选品专家。适用于寻找满足月销量和环比增长阈值的商品、快速上升机会、排序切换、重复巡检、定时任务和仅 Excel 交付的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product research operators use this skill to find sales-surge product candidates, preview top results, export full results to Excel, optionally run preference-based ASIN scoring, and configure repeat scouting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox credentials and can access account-linked product search, text generation, upload, and scheduling services.

Mitigation: Install only for trusted users and environments, scope credentials appropriately, and rotate or remove credentials when access is no longer needed.

Risk: The bundled upload helper can create publicly accessible URLs for local files.

Mitigation: Upload only files intended for public sharing and review exported product data before publishing it.

Risk: The scheduler helper can create recurring agent tasks that continue running after setup.

Mitigation: Confirm frequency, cost, task content, and notification targets before enabling scheduled runs; periodically review and disable unneeded tasks.

Risk: The artifact includes instruction-patching and skill-modification paths beyond the core scouting workflow.

Mitigation: Avoid those paths unless they are intentionally required, and review any proposed instruction changes before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-sales-surge-product-scout)
- [SellerSprite product search API reference](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [Amazon product scout API parameter catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [ASIN dynamic scoring example expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [LinkFox task scheduler API reference](artifact/skills/linkfox-task-scheduler/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON summaries, Excel file paths, and task configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary scouting and scoring deliverables are Excel files; helper flows may create local JSON data, scheduled task configurations, or public file URLs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
