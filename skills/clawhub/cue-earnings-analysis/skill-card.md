## Description:

用 Cue 对上市公司最新财报做深度分析——从营收利润变动、业务驱动、利润含金量、产业链话语权到财务风险信号，产出一份带来源出处的业绩点评，帮个人投资者看懂一家公司的盈利情况，作为选股和股票分析的一环。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors and analysts use this skill to generate sourced earnings commentary for publicly listed A-share, Hong Kong, and U.S. companies after financial reports are disclosed. It helps compare core metrics, business drivers, cash quality, bargaining position, and financial risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned remote repository code under their user account.

Mitigation: Pin and review a specific commit of the Cue runner before execution.

Risk: The setup stores the Cue API key in a local plaintext config file.

Mitigation: Prefer an environment variable or a file with restrictive permissions, and rotate the key if exposed.

Risk: Financial prompts and reports may contain confidential or regulated information.

Mitigation: Avoid submitting confidential, personal, or regulated financial information to Cue prompts or reports.

Risk: Outputs can include Cue links and credit or payment notices.

Mitigation: Review generated reports and user-facing error guidance before sharing externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-earnings-analysis)
- [Cue platform](https://cuecue.cn)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key management](https://cuecue.cn/api-key)
- [CNINFO](https://www.cninfo.com.cn)
- [Eastmoney financial reports](https://data.eastmoney.com)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and Cue share URL, plus bash command snippets for setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and template_id template_7qiAwz; report quality and timeliness depend on Cue service availability and public financial data sources.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
