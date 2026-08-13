## Description:

研技Skill — 获取个股K线数据、成交量、价格走势

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to fetch a lightweight Chinese stock quote summary and view clearly labeled moving-average estimates for teaching or workflow demonstrations. It should not be used as historical K-line analysis or as a basis for trading decisions without a real historical market data source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Moving-average values are simulated estimates and are not derived from historical K-line data.

Mitigation: Treat these indicators as teaching or workflow examples only, and use a real historical market data source before making trading or formal financial decisions.

Risk: Live quote retrieval depends on network access to Sina Finance and can fail or be unavailable.

Mitigation: Check the output data source and failure messages before relying on the result, and avoid assuming failed retrievals contain current market data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanji-kline-data)
- [Publisher profile](https://clawhub.ai/user/caoling7878-arch)
- [Sina Finance real-time quote endpoint](http://hq.sinajs.cn/list={code})
- [Sina Finance](https://finance.sina.com.cn)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a Python command-line script, with guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs disclose whether live Sina Finance data was available and that moving averages are demonstration estimates rather than historical indicators.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
