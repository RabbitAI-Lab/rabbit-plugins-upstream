## Description:

每天开盘前 3 分钟，看懂今天 A 股的机会与风险，自动扫隔夜美股、政策、产业新闻，用大白话讲清利好利空并排出今日值得关注的方向清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a Cue-powered pre-market A-share opportunity and risk report before market open. It helps summarize overnight global events, policy and industry news, affected sectors, opportunity rankings, risk notes, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to run unpinned external runner code.

Mitigation: Review or pin the Cue runner repository before execution and install it only when the user trusts Cue/sensedeal.

Risk: The skill requires a Cue API key stored in a local configuration file.

Mitigation: Protect the API key file, avoid exposing it in logs or shared outputs, and regenerate the key if it may have been disclosed.

Risk: The skill may send private trading plans or proprietary context to an external service.

Mitigation: Avoid including confidential trading plans, proprietary research, account information, or other sensitive data in Cue queries.

Risk: The skill expects Cue share links and credit or payment guidance in agent responses.

Mitigation: Tell the agent when links should be omitted, and review generated responses before sharing them externally.

Risk: The report is based on public information and external service availability, so it can be incomplete, delayed, or unsuitable as investment advice.

Mitigation: Treat the output as research support only, verify important claims with primary market sources, and do not use it as the sole basis for trading decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [ClawHub Publisher Profile](https://clawhub.ai/user/panting09266-ai)
- [Cue API Key](https://cuecue.cn/hub/api-key)
- [Cue Runner Repository](https://github.com/sensedeal/cue-skills)
- [Cue Payment Page](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with inline shell commands, links, and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main report is generated through the Cue runner and may include a Cue share link when a real conversation ID is returned.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
