## Description:

用 Cue 穿透公募基金组合的底层持仓，检测个股重叠、行业集中度、风格暴露和重复配置风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人基金投资者、基金投顾、理财经理和 FOF 研究员可用该技能分析 A 股公募基金组合的底层持仓重叠、行业集中度和风格暴露，并生成组合诊断与调仓参考报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cue queries and generated reports can contain financial or private portfolio information.

Mitigation: Use a trusted Cue service account, avoid shared or cloud-synced report folders for client or personal portfolio reports, and handle outputs as sensitive financial data.

Risk: Portfolio look-through depends on public fund disclosures and an external Cue service, so results may be delayed, incomplete, or unavailable during service or disclosure gaps.

Mitigation: Review the report's source links and data cutoff dates, run the documented health checks when service issues occur, and treat outputs as diagnostic support rather than future performance predictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue service](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnostic report with optional Word or PDF conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include fund holdings, overlap matrices, industry concentration, style exposure, concentration risk ratings, adjustment suggestions, source links, and data cutoff dates.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
