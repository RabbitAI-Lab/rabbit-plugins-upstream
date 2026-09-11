## Description:

每天开盘前 3 分钟，看懂今天 A 股的机会与风险，自动扫隔夜美股、政策、产业新闻，并用通俗语言整理利好利空和今日关注方向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and market researchers use this skill before the A-share market opens to turn overnight global market, policy, and industry news into a concise pre-market opportunity and risk report. The output is informational market research and should not be treated as investment advice or a guarantee of price movement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned remote Python runner.

Mitigation: Install only after reviewing the sensedeal cue-skills runner and pinning it to a reviewed commit.

Risk: The setup flow stores a Cue API key in plaintext.

Mitigation: Store the API key with owner-only permissions and rotate it if it may have been exposed.

Risk: Market research output may be delayed, incomplete, or affected by Cue service and public data source availability.

Mitigation: Treat the report as informational research, verify important claims against market sources, and avoid using it as sole investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [Cue example report](https://cuecue.cn/share/jwhaQSVxNzzWYOvHmt-jO)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a pre-market opportunity and risk report; report quality and timeliness depend on Cue service availability and public data source availability.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
