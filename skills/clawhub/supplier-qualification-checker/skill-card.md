## Description:

This skill helps procurement and project teams assess supplier qualifications and delivery capacity using Zhiliaobiaoxun bidding data, producing single-company due diligence reports or two-company comparisons with sourced findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, tender owners, general contractors, and buyers use this skill to vet a company before onboarding, supplier selection, subcontractor review, or competitive comparison. It queries bidding records, partnership patterns, delivery evidence, and public risk signals to produce a sourced due diligence report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names and query terms are sent to Zhiliaobiaoxun services for lookup and report generation.

Mitigation: Use the skill only for company due diligence queries appropriate for that service, and avoid entering unrelated confidential local file contents or secrets.

Risk: Automatic trial registration may use a MAC-derived device hash for duplicate-trial prevention.

Mitigation: Only run automatic registration after explicit user consent, and keep collection limited to platform, CPU architecture, and SHA256-hashed MAC data as documented.

Risk: The API key may be stored in a local plaintext configuration file.

Mitigation: Prefer a user-managed ZLBX_API_KEY where practical, restrict local config file permissions, and never echo API keys into conversation output or reports.

Risk: Generated HTML reports and signed sk links can be shareable and access-bearing.

Mitigation: Treat generated reports and signed links as sensitive business artifacts, preserve returned links only when needed for citations, and share them only with intended recipients.

Risk: Supplier reports discuss real organizations and may affect commercial decisions.

Mitigation: Keep factual findings sourced, separate facts from inferences, include data-boundary notes, and avoid accusatory or unsupported wording.

Risk: Contact data may be returned in masked or full form depending on account status.

Mitigation: Display contact data exactly as returned by the service, do not reconstruct masked details, and do not batch-export contact lists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Enterprise Intelligence Workflow](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Automatic Registration Flow](references/auto-register.md)
- [Report Template](references/report-template.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Account and Registration Base](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report text plus self-contained HTML report files generated from structured JSON input.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY. May write HTML reports under ~/zlbx-company-intel-files/. Reports include sourced findings, data-boundary notes, and signed API-returned links when present.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
