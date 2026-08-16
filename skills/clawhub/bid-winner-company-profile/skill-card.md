## Description:

Helps agents investigate a named company’s public bid-winning history, performance evidence, fulfillment record, customer and supplier ecosystem, competitors, and public risk signals using Zhiliaobiaoxun bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and developers use this skill to turn a company name or company link into a traceable bidding-performance due-diligence report. It supports single-company reports and two-company comparisons for qualification checks, supplier review, competitive analysis, and performance-history verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses a vendor API key locally.

Mitigation: Preconfigure ZLBX_API_KEY where possible, protect local credential files, and never paste API keys into chat output.

Risk: Generated HTML reports and preserved sk links may provide access-bearing report, company, or announcement views.

Mitigation: Treat report files and sk links as private materials and share them only with intended recipients.

Risk: Contact lookups can involve sensitive business contact information.

Mitigation: Request contact lookups only with a valid business or legal basis and preserve the vendor-returned masking without enrichment.

Risk: Auto-registration collects limited device attributes for free-trial deduplication.

Mitigation: Require explicit user consent before registration and preconfigure ZLBX_API_KEY to avoid auto-registration entirely.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile)
- [Workflow Reference](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Reference](references/auto-register.md)
- [HTML Report Renderer](scripts/render_report.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional local HTML report file and user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs preserve API-returned source links, disclose data boundaries, and may include a generated report file path.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
