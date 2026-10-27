## Description:

整理商家提供的至多100行商品名称、颜色、尺寸和型号资料，输出统一命名表、重复与缺失规格报告及含待确认原因的CSV导入草稿；保留原字段和行顺序，重复组所有行均需确认，缺少关键值时先请求补齐，不读取店铺后台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文小店经营者及整理商品资料的创作者，帮助他们核对最多100行商品名称、颜色、尺寸和型号，标出重复、缺失与待确认项，并生成可人工复核的CSV导入草稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A CSV draft may contain unresolved duplicates, missing values, or naming questions.

Mitigation: Review the CSV and resolve flagged items before importing it yourself.

Risk: An installation command may use a changing installer version or repository revision.

Mitigation: Review and pin the installer version and repository revision where supported.

## Reference(s):

- [商品规格与SKU整理 ClawHub 页面](https://clawhub.ai/xxjrq/skills/shop-sku-normalizer-cn)
- [ERPNext 公共项目](https://github.com/frappe/erpnext)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Guidance]

**Output Format:** [Markdown tables and a copyable CSV draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 100 user-supplied rows; preserves source fields and order, flags unresolved items, and does not access shop systems or import data.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
