## Description:

使用 GPT Image 2 按缺陷工单局部精修商品照片：为每个问题指定编辑区域、QC事实源和验收标准，同时保护SKU、结构、材质、Logo、包装、人物与构图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and product-image editors use this skill to create controlled local-retouch tickets for commercial product photos, with explicit defect zones, QC truth sources, preservation constraints, and acceptance criteria before sending images to AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI Hive API keys may be exposed if pasted into command history or stored insecurely.

Mitigation: Prefer AI_HIVE_API_KEY or the protected config file path, and avoid pasting secrets into shared shells or logs.

Risk: Product and QC images are uploaded to AI Hive when the retouch command is run.

Mitigation: Use the skill only for images that are approved for upload to AI Hive, and run --preview first when checking prompts or cost-sensitive jobs.

Risk: Generated edits may change product facts, packaging text, color, model identity, or unapproved image regions.

Mitigation: Compare the output against the original and QC sources, verify each acceptance criterion, and reject outputs that alter unlisted areas or product facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/image-2-product-retouch)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON preview output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper submits one GPT Image 2 retouch task at a time, can preview the generated prompt without upload, and can save generated image files from AI Hive.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
