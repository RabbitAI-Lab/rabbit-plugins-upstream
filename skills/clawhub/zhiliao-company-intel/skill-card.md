## Description:

Generates bid-data-backed company intelligence and background-check reports covering business focus, customer and supplier relationships, award history, competitors, public risk signals, and a local HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and due-diligence users can use this skill to turn a company name or company link into a bid-data-backed intelligence report for supplier review, competitor analysis, customer background checks, or lightweight due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, query terms, and related business-intelligence requests are sent to a third-party vendor service.

Mitigation: Use the skill only when that data sharing is acceptable for the task and avoid submitting sensitive internal context beyond the company-query data needed.

Risk: Automatic registration may use a MAC-derived device hash for free-trial de-duplication.

Mitigation: Run automatic registration only after explicit user consent; skip it by providing ZLBX_API_KEY or a local ~/.zlbx/config.json credential.

Risk: The skill handles API credentials through the environment or ~/.zlbx/config.json.

Mitigation: Protect the local configuration file, prefer user-managed credentials, and do not print API keys in agent responses or generated reports.

Risk: Generated HTML reports and signed vendor links may expose report details or direct access to vendor pages when shared.

Mitigation: Share generated reports only with intended recipients and treat embedded links as potentially access-granting vendor URLs.

Risk: Company background reports can affect real organizations if unsupported or overly conclusive language is used.

Mitigation: Keep claims tied to cited bid records or public sources, separate facts from inference, and present public-risk items as source-backed statements rather than accusations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel)
- [API quick reference](artifact/references/api-quick.md)
- [Company intelligence workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Zhiliao Biaoxun API v2](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliao AI Open Platform](https://ai.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation, self-contained HTML report file, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; generated reports may include cited company and bid URLs returned by the vendor service.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
