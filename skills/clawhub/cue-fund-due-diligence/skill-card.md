## Description:

用 Cue 一键给一只基金做全维度深度体检，包括基金经理画像、业绩归因、风格一致性、风险指标、费率与规模，帮助判断历史业绩更像来自能力还是市场环境。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, financial advisers, and fund researchers use this skill to request Cue-based due diligence on A-share public equity funds. It supports fund selection, holding diagnosis, fund manager assessment, and replacement-fund screening by producing a structured analysis of manager profile, attribution, style consistency, risk, holdings, fees, and scale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Cue's external service for fund analysis and depends on Cue service availability and data freshness.

Mitigation: Confirm Cue service health before running and treat unavailable or stale results as a reason to retry later or use the documented manual research sources.

Risk: The skill requires a Cue API key that is stored locally or supplied through the environment.

Mitigation: Have the user create and manage their own key, avoid printing secrets, and do not share logs that might expose API keys or private report links.

Risk: The setup flow installs or updates Cue runner code from external repositories.

Mitigation: Review the referenced runner source and install only if the user accepts mutable external code as part of the workflow.

Risk: Fund due-diligence output can influence investment decisions but is not guaranteed financial advice.

Mitigation: Present results as research support, preserve source links and data cutoff dates, and encourage independent review before acting.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [Publisher Profile](https://clawhub.ai/user/panting09266-ai)
- [Cue Service](https://cuecue.cn)
- [Cue API Key Setup](https://cuecue.cn/hub/api-key)
- [Cue Runner Repository](https://github.com/sensedeal/cue-skills)
- [Cue Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and setup or recovery commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a fund name or code and should preserve the generated report, data cutoff date, and Cue report link when available.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
