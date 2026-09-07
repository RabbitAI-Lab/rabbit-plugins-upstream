## Description:

政府采购投标决策分析助手，基于知了标讯招中标历史数据，为具体政采类招标项目评估是否投标、限制性信号、采购方偏好、竞争对手、历史成交价、建议报价和合规风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, bid teams, and procurement analysts use this skill to evaluate a specific Chinese government procurement opportunity before deciding whether and how to bid. The skill produces a decision report covering project fit, buyer history, likely competitors, pricing reference points, data gaps, and compliance-sensitive risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a vendor trial account after user consent and collect a hashed MAC address for device deduplication.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when available; otherwise require explicit user consent and present the stated device-feature collection limits before registration.

Risk: The skill stores and uses a vendor API key and may write configuration under the user's home directory.

Mitigation: Do not ask users to paste API keys into chat, avoid exposing credentials in responses or logs, and review local credential storage before deployment.

Risk: Generated HTML reports can include signed links returned by the vendor service, which may provide access intended only for the recipient.

Mitigation: Preserve returned links for traceability but avoid sharing generated reports beyond intended audiences when signed links may grant access.

Risk: The security scan flags the skill as suspicious because it combines bid analysis with account creation, device fingerprinting, credential storage, local report generation, and vendor links.

Mitigation: Review the skill before installation, confirm that vendor domains and promotional links are acceptable, and deploy only where these behaviors match user expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision)
- [ClawHub publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Skill definition](artifact/SKILL.md)
- [Bid analysis workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration workflow](artifact/references/auto-register.md)
- [HTML report renderer](artifact/scripts/render_report.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional local HTML report file and supporting JSON input for report rendering]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for vendor API access; full analysis is documented as about 12-25 API calls and quick analysis as about 5-8 API calls.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
