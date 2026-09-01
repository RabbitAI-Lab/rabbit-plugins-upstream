## Description:

依据已保存的 Amazon 商品快照和确定性 Diff，按已支持周期提醒标题、要点、图片等商品页字段变化；仅用于变化提醒，不用于小时级监控、付费 LLM 分析、自动修改页面或推断销量、库存、订单和真实退货率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon marketplace operators and agent users use this skill to list, create, pause, resume, delete, and review saved product-listing snapshot watches for supported ASINs. It helps surface deterministic changes to listing fields such as title, bullets, and images without making listing edits or providing real-time sales, inventory, order, advertising, or return-rate data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI exposes broader account, export, mutation, and paid AI operations beyond the advertised listing-change workflow.

Mitigation: Review the package before installing and use only the documented watch commands for this skill.

Risk: The skill requires an ARI API key, and custom ARI endpoint settings could redirect authenticated requests if misused.

Mitigation: Protect the ARI API key and avoid setting ARI_BASE_URL or ARI_ALLOW_CUSTOM_BASE unless you control the endpoint.

Risk: Daily or weekly watches may have quota or cost implications.

Mitigation: Check account quota and cost implications before enabling or changing watch schedules.

## Reference(s):

- [Amazon Listing 变化提醒 专用监控参考](references/reference.md)
- [Amazon Listing 变化提醒 专用监控工作流](references/watch-workflow.md)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/listing-change)
- [Publisher profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; documented watch digest output is deterministic and reports zero credits used.]

## Skill Version(s):

1.4.3 (source: frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
