## Description:

研林Skill - 采集A股大盘指数、行业板块排名、核心权重股行情数据.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch current A-share market index quotes, sector rankings, concept rankings, and core stock quotes for market-monitoring workflows. The data is suitable for situational awareness and should be verified before financial decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live market data from third-party finance websites may be delayed, unavailable, or inaccurate.

Mitigation: Verify time-sensitive data against authoritative market data sources before making financial or trading decisions.

Risk: The skill contacts external finance websites during execution.

Mitigation: Review network access expectations before installation and run it only in environments where public finance-site requests are permitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanlin-market-data)
- [Sina Finance quote endpoint](https://hq.sinajs.cn/list={codes})
- [Sina Finance](https://finance.sina.com.cn)
- [Tonghuashun sector rankings](http://q.10jqka.com.cn/thshy/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON market data emitted by a command-line script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches public market data from Sina Finance and Tonghuashun without credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
