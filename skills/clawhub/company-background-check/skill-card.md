## Description:

This skill helps agents produce procurement-data-centered company background reports from a company name, including business profile, customer and supplier relationships, bid-winning strength, competitors, public-risk checks, and optional contact channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and due-diligence users use this skill to assess a company from public tender and award data before cooperation, competition, or supplier review. It supports single-company reports and two-company comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries are sent to Zhiliaobiaoxun services.

Mitigation: Install only when sharing searched company names and query criteria with Zhiliaobiaoxun is acceptable.

Risk: Automatic registration uses a stable MAC-derived device hash for trial-account deduplication.

Mitigation: Prefer a user-provided ZLBX_API_KEY to bypass automatic registration, or review the registration prompt before consenting.

Risk: The skill stores API credentials in ~/.zlbx/config.json.

Mitigation: Keep the configuration file private to the local user account and avoid exposing API keys in conversation or shared files.

Risk: Generated HTML reports, signed sk links, auto-login links, and contact phone numbers can expose sensitive business information.

Mitigation: Limit sharing of generated reports and links, and treat contact information according to the privacy level returned by the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Seven-step company intelligence workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration workflow](artifact/references/auto-register.md)
- [HTML report renderer](artifact/scripts/render_report.py)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliaobiaoxun agent platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with optional self-contained HTML files and JSON report data for rendering.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports include cited source links when available and may include local HTML report paths.]

## Skill Version(s):

1.0.4 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
