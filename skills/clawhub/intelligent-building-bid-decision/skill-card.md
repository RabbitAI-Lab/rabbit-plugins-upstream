## Description:

Assists bidders on weak-current, security-monitoring, and intelligent-building projects with go/no-go decisions, buyer history, competitor prediction, pricing reference, qualification checks, and bid-risk assessment using Zhiliaobiaoxun bid data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External commercial bidders and bid teams use this skill to evaluate whether to pursue a specific security-monitoring or intelligent-building tender, estimate likely competitors, compare historical prices, and produce a decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party vendor API for bid data and account operations.

Mitigation: Review the vendor API relationship before installation and use a self-managed ZLBX_API_KEY when available.

Risk: Free-trial registration may use consent-gated device fingerprinting for de-duplication.

Mitigation: Require clear user consent before registration, or preconfigure ZLBX_API_KEY to bypass auto-registration.

Risk: API credentials may be stored locally in ~/.zlbx/config.json.

Mitigation: Prefer environment-variable configuration for managed environments and restrict access to any local credential file.

Risk: Generated HTML reports may include signed links that allow recipients to access linked bid records.

Mitigation: Remove signed links before forwarding reports unless the recipient is intended to access those records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](artifact/references/api-quick.md)
- [Bid Decision Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration Flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, JSON, Files, Guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report and structured citation data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY; full analysis is documented as roughly 12-25 vendor data queries, while quick analysis is roughly 5-8 queries.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
