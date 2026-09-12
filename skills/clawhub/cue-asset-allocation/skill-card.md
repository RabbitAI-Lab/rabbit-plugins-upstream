## Description:

用 Cue 一键生成月度大类资产配置报告——整合全球 CPI、利率、国内宏观及资金流向，从宏观逻辑推导至股/债/商配置比例，产出可交付客户的配置建议书。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisers, investment teams, and agents use this skill to run a Cue workflow that produces a monthly macro asset-allocation report for stocks, bonds, and commodities. It is suited for client allocation memos, investment committee drafts, and portfolio rebalancing analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an external Cue runner with local credentials.

Mitigation: Install only if you trust Sensedeal/Cue, inspect the runner source before execution, and consider using a dedicated Cue API key with limited exposure.

Risk: Allocation prompts and related investment context are sent to cuecue.cn.

Mitigation: Avoid confidential client data in prompts and review data-sharing requirements before use.

Risk: Financial report quality and timeliness depend on Cue service status and external data sources.

Mitigation: Review report assumptions, source links, and risk disclosures before using outputs for client or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-asset-allocation)
- [Cue sample asset-allocation report](https://cuecue.cn/share/JJiW9tVCEK7Yq3AW0zDnw)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report written to a local file, with optional DOCX or PDF conversion commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report quality and freshness depend on Cue service availability and external data sources.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
