## Description:

结合 Amazon 商品详情与评论证据，按影响程度规划产品升级方向和验证问题；仅用于产品升级规划，不用于销量预测、采购下单或自动改版执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to turn product details and review evidence into prioritized upgrade directions, validation questions, and account-backed reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key to access ARI account data and Amazon review-analysis workflows.

Mitigation: Install only when the user is comfortable granting ARI access; keep keys out of prompts, reports, and command examples, and stop on authentication or credit errors.

Risk: Some operations can spend account credits or change future collection, monitoring, competitor, or autoconfirm behavior.

Mitigation: Use explicit quote-only wording for pricing checks, keep autoconfirm set to ask for per-action control when needed, and require clear user approval before schedule, watch, competitor, or confirmed paid actions.

Risk: Interrupted paid operations may already have charged credits or created a report.

Mitigation: Check existing reports or operation status with the documented read-only commands before retrying a confirmed paid operation.

## Reference(s):

- [Operation Workflow Reference](references/operation-workflow.md)
- [ARI Command and API Reference](references/reference.md)
- [ARI API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-upgrade)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and account or API status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; may create paid reports, export files, and manage monitoring-related settings through the documented confirmation flow.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
