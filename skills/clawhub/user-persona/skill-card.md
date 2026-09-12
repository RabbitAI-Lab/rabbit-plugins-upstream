## Description:

从 Amazon 评论中提炼买家画像、使用场景、购买动机、替代来源和广告文案洞察，并通过 ARI 生成摘要、报告和可导出的资料。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to understand who buys a product, why they buy it, which situations they use it in, and how review evidence can inform positioning, ads, copy, competitive comparison, and product improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an ARI API key locally and can access ARI account data.

Mitigation: Use browser authorization or hidden terminal input, do not paste API keys into chat, and revoke or recreate the key from the ARI account page if access should change.

Risk: Some ARI flows can generate paid reports under account auto-confirm rules.

Mitigation: Ask for quote-only behavior when checking cost, set auto-confirm off for every paid action, and require explicit confirmation before commands that are not covered by a deliberate account rule.

Risk: The skill can change monitoring or confirmation settings and those settings may affect future costs.

Mitigation: Confirm schedule, cost, and auto-confirm changes with the user before applying them, and restate the active setting after any change.

Risk: Interrupted paid analysis may already have been charged and archived.

Mitigation: Check existing reports or operation status before retrying any paid command, and only rerun after confirming that no report was generated.

Risk: Review analysis can be misleading when samples, time windows, variants, or marketplace coverage are limited.

Mitigation: Report sample size, site, date window, and data gaps, and avoid treating missing or incomplete review data as evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/user-persona)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [Account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [Billing and plans](https://ari.funewa.com/zh/billing)
- [Product management](https://ari.funewa.com/zh/products)
- [Report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown prose with optional bash commands, JSON command results, and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may create local exports when the user requests report or review downloads.]

## Skill Version(s):

1.4.8 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
