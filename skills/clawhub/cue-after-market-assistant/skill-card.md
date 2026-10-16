## Description:

为个人投资者生成 A 股收盘后的大盘与板块复盘，梳理涨跌原因、资金流向和次日观察要点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人投资者可在收盘后查看大盘和板块表现、资金动向及持仓可能受到的市场层面影响，并准备次日观察清单；不用于个股技术分析或盘前预测。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Cue API key and an external runner that is downloaded or updated before use.

Mitigation: Install only if comfortable with the Cue service and runner; create and manage the key yourself and review the runner before execution.

Risk: Automating the suggested daily recap creates recurring external-service use.

Mitigation: Approve any scheduled task separately before enabling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn/)
- [Cue API key registration](https://cuecue.cn/api-key?src=clawhub-after-market-assistant)
- [Cue runner dependency](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Seven-section Markdown market recap with a link to the original report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Markdown copy; optional Word or PDF conversion.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
