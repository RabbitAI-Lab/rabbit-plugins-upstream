## Description:

订阅 Amazon ASIN 后，ARI 持续监控差评突增和星级下滑，并在会话内读取预警、定位问题评论、生成根因分析与回复建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce operators use this skill to monitor ASIN review sentiment, investigate negative review spikes, generate VOC and operations reports, and manage ARI review-analysis workflows from an agent chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through paid workflows and account auto-confirm behavior.

Mitigation: Use quote-only checks for price requests, keep auto-confirm off when review is preferred, and require explicit confirmation before running confirmed paid operations.

Risk: The skill can change persistent account settings, monitoring schedules, competitor relationships, and workbench status through chat-driven workflows.

Mitigation: Treat schedule, watch, autoconfirm, competitor, and status-changing actions as management changes and execute them only after the user explicitly requests the exact change.

Risk: Interrupted paid workflows may already have charged credits or generated reports.

Mitigation: Check existing reports or workflow status before retrying any confirmed paid workflow.

Risk: The skill requires ARI account access and an API key.

Mitigation: Use browser authorization or local configuration only, never request passwords, and do not include API keys in reports, examples, or chat output.

Risk: Review analysis depends on ARI-collected Amazon review samples that may not cover every review, variant, or time window.

Mitigation: State the sample range and data limits in outputs, and avoid presenting unsupported trends or variant coverage as fact.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-alerts)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [ARI Amazon 评论智能助手使用指南](artifact/使用说明.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown with inline shell commands, JSON snippets, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state data ranges and limits, preserve user confirmation boundaries for paid actions, and avoid exposing API keys.]

## Skill Version(s):

1.4.13 (source: server release, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
