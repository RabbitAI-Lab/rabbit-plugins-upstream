## Description:

AI投标策略顾问 uses ZhiLiao Biaoxun tender and award data to help assess a specific bidding opportunity, including bid/no-bid posture, pricing strategy, competition, buyer patterns, win probability, risks, and action recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External bid, sales, and business development teams use this skill to analyze a concrete tender and produce a decision-oriented strategy report. It is most useful when the user provides a tender link, title, or file and wants guidance on whether to bid, how to price, and which competitors may appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store an API key locally for later use.

Mitigation: Prefer a preconfigured ZLBX_API_KEY where possible and check permissions on ~/.zlbx/config.json if a local key is written.

Risk: Generated HTML reports and signed sk or auto-login links may expose sensitive account or report access.

Mitigation: Treat generated reports and signed links as sensitive, avoid broad sharing, and preserve links only for intended recipients.

Risk: Automatic registration can collect a stable device fingerprint.

Mitigation: Use a preconfigured API key to avoid automatic device registration, or proceed only after informed user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [ZhiLiao Biaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiao Biaoxun account endpoint](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited tender or company records, API-derived amounts and dates, a local HTML report path, and original source links returned by the data service.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
