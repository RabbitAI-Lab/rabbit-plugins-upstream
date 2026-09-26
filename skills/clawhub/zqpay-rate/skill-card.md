## Description:

查询各国汇率，在用户询问汇率、货币兑换或国家/地区货币换算时解析币种并查询 zqpay-rate 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[greenteawater](https://clawhub.ai/user/greenteawater)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Chinese-language exchange-rate and currency-conversion questions by mapping currency names to ISO codes, querying the declared zqpay-rate service, and formatting rate details with timestamps. It is for informational exchange-rate lookup, not for fees, limits, or high-value foreign-exchange business rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Currency-pair queries are sent to the declared zqpay exchange-rate service.

Mitigation: Install only when that data flow is acceptable for the deployment, and avoid submitting sensitive transaction context beyond the currency pair needed for lookup.

Risk: The security evidence reports one incorrect example that could produce an inaccurate quote.

Mitigation: Verify important rates against the live API response and source timestamp, and require publisher correction of the CNY/USD example before relying on the skill for precise financial information.

Risk: The skill provides informational rates and does not cover fees, limits, or foreign-exchange business rules.

Mitigation: Use the output as rate guidance only and direct users to appropriate financial or compliance channels for transactional decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/greenteawater/skills/zqpay-rate)
- [Declared zqpay-rate API endpoint](https://aipaytest.zqpay.com/zl-core-rate-crawler/api/rates/latest)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown-style Chinese text with exchange-rate tables, timestamps, warnings, and optional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include a required platform service line and may include warnings for reverse-calculated or unavailable currency-pair data.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
