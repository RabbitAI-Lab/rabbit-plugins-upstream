## Description:

医疗器械投标决策分析助手，用于根据医疗类招标项目和全网招中标历史数据，输出是否应该投标、采购方偏好、竞争对手预测、报价参考和废标风险评估。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, bidding, and procurement teams use this skill to assess whether to bid on a specific hospital or health-system procurement project, estimate competitive pricing, identify likely competitors, and produce a concise decision report from public tender history.

### Deployment Geography for Use:

Global, with analysis focused on China medical procurement and tender data.

## Known Risks and Mitigations:

Risk: The skill depends on a third-party vendor API and requires a ZLBX API key.

Mitigation: Review the vendor service before installation and prefer a preconfigured API key when account control matters.

Risk: The skill can persist credentials locally and save generated reports on disk.

Mitigation: Store the API key only in approved local locations and restrict access to generated report files.

Risk: Generated report and platform links may include signed access parameters.

Mitigation: Treat signed links as sensitive and avoid forwarding reports or links beyond the intended audience.

Risk: Automatic registration may collect limited device characteristics for trial-account deduplication.

Mitigation: Use a preconfigured ZLBX_API_KEY to avoid device-based auto-registration when that collection is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/medical-device-bid-decision)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration guidance]

**Output Format:** [Markdown decision report, with optional HTML report file generated from structured report data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report should put the recommendation first, cite the tender data used for conclusions, mark data gaps, and include a disclaimer.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
