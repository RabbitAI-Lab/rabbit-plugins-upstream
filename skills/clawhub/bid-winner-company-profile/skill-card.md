## Description:

This skill helps agents produce Chinese company due-diligence reports from public bidding and procurement records, including bid history, performance evidence, customer and supplier relationships, competitors, public risk signals, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, sales teams, procurement reviewers, and agents use this skill to assess a company from a bidding-history perspective. It supports single-company deep reports and two-company comparisons with traceable bid records and cited public-risk statements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company-query data is sent to a third-party vendor API.

Mitigation: Install only when that data sharing is acceptable for the organization and avoid submitting sensitive company queries without approval.

Risk: The skill handles API credentials and may use consent-based auto-registration with a stable hashed device identifier.

Mitigation: Prefer a managed ZLBX_API_KEY secret or environment variable, and use auto-registration only after explicit user consent.

Risk: Generated reports may contain signed source links and contact phone data.

Mitigation: Review HTML and Markdown reports before sharing, avoid forwarding reports containing sk links, and request contact lookups only for legitimate business reasons.

Risk: The report renderer writes local HTML files by default.

Mitigation: Store generated reports in approved locations and remove files that contain sensitive company, contact, or signed-link data when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)
- [Report renderer](artifact/scripts/render_report.py)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Chinese Markdown report plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; reports may include signed source links and contact fields returned by the vendor API.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
