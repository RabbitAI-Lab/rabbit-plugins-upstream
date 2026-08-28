## Description:

查询公司海关贸易HS编码维度统计数据，分析HS编码分布、贸易量分解和月度贸易趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams and agents use this skill to query Upkuajing customs data for a company and analyze trade composition by HS code, including monthly trends, trade counts, and HS-code share. It supports category analysis and supply-chain decisions that depend on company-level import/export product distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an Upkuajing API key and may store that key in ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, keep the file private, avoid sharing the key in prompts or reports, and rotate the key if exposure is suspected.

Risk: Normal HS-code statistics queries are paid API calls.

Mitigation: Tell the user that the query will incur a charge and wait for explicit confirmation before executing paid calls.

Risk: Recharge flows can expose users to payment links and account-balance decisions.

Mitigation: Present recharge links as Upkuajing payment actions, ask users to verify the destination before payment, and continue only after the user confirms completion.

Risk: Diagnostic error reports can include business context or request details.

Mitigation: Ask for confirmation before reporting errors and avoid including secrets or unnecessary sensitive business details in diagnostic context.

## Reference(s):

- [公司贸易HS编码维度统计 API 参考](references/customs-company-hscode-stats-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Developer Platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-stats-zh)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and formatted JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful queries include data, fee information, and requestId.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter metadata, release evidence, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
