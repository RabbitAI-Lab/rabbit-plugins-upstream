## Description:

用 Cue 对上市公司最新财报做深度分析——从营收利润变动、业务驱动、利润含金量、产业链话语权到财务风险信号，产出一份带来源出处的业绩点评，帮个人投资者看懂一家公司的盈利情况，作为选股和股票分析的一环。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors use this skill to review publicly disclosed financial statements for listed companies and understand reported performance, business drivers, cash-flow quality, supply-chain position, and financial warning signs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions ask users to paste their Cue API key into chat, which can expose the credential.

Mitigation: Configure the key locally with owner-only file permissions, avoid sharing it in chat, and replace any key already shared there.

Risk: The workflow installs and runs an external research runner, and sends research queries and reports to Cue, where service credits may be consumed.

Mitigation: Review and pin the runner before execution, and ensure users understand that queries and reports are processed by Cue and consume credits.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-earnings-analysis)
- [Cue runner source listed in the skill documentation](https://github.com/sensedeal/cue-skills)
- [Gitee mirror listed in the skill documentation](https://gitee.com/sensedeal/cue-skills)
- [China Securities Regulatory Commission Information Disclosure website](https://www.cninfo.com.cn)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured Markdown earnings commentary with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers publicly disclosed financial statements and includes source links in the report.]

## Skill Version(s):

1.0.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
