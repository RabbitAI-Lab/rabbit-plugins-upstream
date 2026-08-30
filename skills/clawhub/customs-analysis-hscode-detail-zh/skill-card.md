## Description:

根据指定 HS 编码查询中英文描述信息，帮助贸易、分析和进出口用户理解该编码对应的产品类别。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade professionals, analysts, import/export operators, and agents use this skill to look up the Chinese and English description for a known HS code before product classification checks, customs-code interpretation, or trade-data analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider API key may be stored in a local plaintext file.

Mitigation: Use a minimally scoped key and verify permissions on ~/.upkuajing/.env.

Risk: HS-code lookups, account actions, and recharge-order flows can involve paid API activity.

Mitigation: Explain the cost-bearing action and wait for explicit user confirmation before running paid or recharge-related commands.

Risk: Troubleshooting reports can send error context to the provider.

Mitigation: Avoid sensitive business data in report context and submit error reports only after user confirmation.

## Reference(s):

- [HS Code Detail API Reference](artifact/references/customs-analysis-hscode-detail-api.md)
- [Skill Error Report API Reference](artifact/references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Developer Platform](https://developer.upkuajing.com/)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-detail-zh)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Natural-language guidance with Python command examples and JSON API responses containing HS-code descriptions, fee details, and request identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY. Paid API calls and recharge actions should be confirmed by the user before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
