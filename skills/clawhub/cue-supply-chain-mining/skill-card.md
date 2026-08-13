## Description:

用 Cue 沿产业链挖掘具备业绩爆发潜力的"隐形冠军"，梳理产业链传导路径，基于基本面与弹性逻辑发现未被充分定价的优质标的。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, research analysts, industry analysts, and market researchers use this skill to study public supply-chain structures, identify lesser-known listed companies, assess fundamentals-driven upside, and prepare research reports. It is intended for fundamental research support, not real-time trading advice or buy/sell recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Cue's external research service and sends the user's query and Cue API key to cuecue.cn.

Mitigation: Use the skill only when external Cue service use is intended, protect the API key, and review organization policy before sending sensitive research topics.

Risk: Generated reports can influence financial decisions but are research outputs rather than trading advice.

Mitigation: Treat results as research support, verify cited sources independently, and avoid using the output as a direct buy, sell, price, or timing recommendation.

Risk: The workflow writes reports locally and may persist session state for resuming interrupted jobs.

Mitigation: Store generated reports and session files in approved locations and remove them according to local data-retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-mining)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Example report](https://cuecue.cn/share/F8PzjKYbVBgYX2oN9clWB)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; reports may be written locally and session state may persist for interrupted jobs.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
