## Description:

货币汇率换算、热门汇率、货币列表、银行外汇牌价、实时行情及历史汇率等。当用户说：100 美元换多少人民币？今天中行美元现汇价？美元人民币最近一周走势？美元指数多少？或类似汇率换算问题时，使用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer exchange-rate questions, convert amounts between currencies, and retrieve current or historical foreign-exchange rates and bank quotes through JisuAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exchange-rate query details and the configured JISU_API_KEY are sent to JisuAPI.

Mitigation: Use the skill only when the user is comfortable using JisuAPI, and avoid including unrelated sensitive personal or account information in prompts.

Risk: Exchange-rate data is provided for reference and may not be suitable as the sole basis for financial decisions.

Mitigation: Present rates as reference data and direct users to verify critical transactions with their bank or financial provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/exchange)
- [ClawHub publisher profile](https://clawhub.ai/user/jisuapi)
- [JisuAPI exchange-rate documentation](https://www.jisuapi.com/api/exchange/)
- [JisuAPI website](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; sends exchange-rate query parameters to JisuAPI.]

## Skill Version(s):

1.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
