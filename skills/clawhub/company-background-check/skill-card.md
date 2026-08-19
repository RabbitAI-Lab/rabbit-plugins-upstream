## Description:

This skill helps agents produce company background-check reports from bid and tender data, including business profile, customers and suppliers, award history, competitors, public-risk findings, and optional contact lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Business, sales, procurement, and partnership users use this skill to review a named company or compare two companies before cooperation, bidding, supplier evaluation, or competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, search terms, and report requests are sent to a paid third-party company-intelligence service.

Mitigation: Install and use the skill only when users are comfortable sending those queries to Zhiliaobiaoxun, and disclose expected credit consumption before running a report.

Risk: The skill can auto-register an account and store credentials locally when no API key is configured.

Mitigation: Require explicit user consent before auto-registration, prefer a user-provided ZLBX_API_KEY when available, and remove ~/.zlbx/config.json if the skill is no longer used.

Risk: Generated HTML reports and signed platform links can expose sensitive business-intelligence results if forwarded broadly.

Mitigation: Treat reports and sk-bearing links as sensitive, restrict sharing, and periodically clean up ~/zlbx-company-intel-files/.

Risk: Company background reports can affect commercial or reputational decisions if interpreted as definitive judgments.

Mitigation: Use the report as a reference, keep facts and inferences separate, attach source links for public-risk statements, and verify important findings against official sources.

Risk: Contact lookup may return masked or full contact data depending on account status.

Mitigation: Display contact data only in the form returned by the service, do not reconstruct masked numbers, and do not bulk-export contact lists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](references/api-quick.md)
- [Workflow guide](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API endpoint template](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s119)
- [Zhiliaobiaoxun business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, optional self-contained HTML report files, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; generated reports may include shareable signed links and should be handled as sensitive.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
