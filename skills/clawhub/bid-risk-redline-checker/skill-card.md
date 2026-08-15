## Description:

废标风险与控标信号识别助手，用于评估具体招标项目的限制性信号、竞争开放度、采购方供应商格局、同类项目对比和投标决策建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to decide whether to pursue a specific bid, estimate pricing posture, identify likely competitors, and document red-line risk signals from public bidding data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists or uses a vendor API key and stores auto-registered credentials under ~/.zlbx/config.json.

Mitigation: Use a preconfigured ZLBX_API_KEY where possible, protect the local config file, and avoid entering or displaying API keys in chat.

Risk: Auto-registration collects limited device-derived attributes after consent.

Mitigation: Confirm user consent before registration and use an existing API key to bypass the auto-registration path when privacy review requires it.

Risk: Generated reports may include signed vendor links that can bypass login for the referenced report or source records.

Mitigation: Treat generated HTML reports and signed links as sensitive and avoid broad redistribution.

Risk: Procurement risk conclusions could be misleading if data is incomplete or phrased as an accusation.

Mitigation: Keep conclusions tied to cited public data, mark data gaps, and use signal-based language rather than definitive misconduct claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Zhiliaobiaoxun registration portal](https://ai.zhiliaobiaoxun.com/?ch=s84)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown procurement risk report, optional self-contained HTML report file, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based vendor registration; full analysis estimates 12-25 API calls and lightweight analysis estimates 5-8 API calls.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
