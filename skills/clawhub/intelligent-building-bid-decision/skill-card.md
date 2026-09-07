## Description:

该技能帮助用户基于知了标讯招中标数据评估弱电智能化、安防监控等项目是否值得投标，并生成报价、竞争、采购方和风险分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to evaluate specific weak-current intelligent building and security-monitoring bids. It helps assess whether to bid, expected competitors, buyer history, pricing benchmarks, qualification risks, and decision rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Zhiliaobiaoxun services and may create or use an account.

Mitigation: Install only after reviewing the service dependency, or provide an existing ZLBX_API_KEY to avoid the automatic account setup path.

Risk: Automatic trial setup collects a hashed MAC address for device deduplication after consent.

Mitigation: Require explicit user consent before account setup and skip the flow when ZLBX_API_KEY or ~/.zlbx/config.json is already configured.

Risk: The skill may save an API key under ~/.zlbx/config.json.

Mitigation: Prefer environment-based credentials where possible and protect or remove the local config file when access should be revoked.

Risk: Generated HTML reports may include signed access links and vendor promotional links.

Mitigation: Avoid sharing generated reports unless the recipient should receive access through the included links.

Risk: Bid recommendations can be affected by data gaps or stale public procurement records.

Mitigation: Review the generated report, check cited source records, and treat the output as decision support rather than a final commercial decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision)
- [Five-step bid decision workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Bid decision report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun automatic registration endpoint](https://ai.zhiliaobiaoxun.com/web-api/internal/auto-register)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report in conversation, with optional local HTML report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based account setup; full reports use about 12-25 API calls and quick checks use about 5-8 API calls.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
