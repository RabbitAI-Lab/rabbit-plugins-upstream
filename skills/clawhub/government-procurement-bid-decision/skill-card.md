## Description:

Assists agents with Chinese government and state-owned-enterprise procurement bid decisions by analyzing project fit, restrictive signals, buyer history, likely competitors, price benchmarks, and compliance risks from bid data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to decide whether to pursue a specific public-sector procurement project, estimate a defensible bid range, and understand likely competitors and red-line risks. Agents use it when a user provides a tender notice, project title, bid ID, or procurement file and asks for a bid/no-bid assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider stores or uses an API key for bid-data access and may persist it in the user's home directory.

Mitigation: Prefer a user-managed ZLBX_API_KEY when available, review local credential storage before installation, and avoid exposing API keys in conversation or reports.

Risk: Consent-based auto-registration uses platform, CPU architecture, and a hashed device identifier to create or reuse a trial account.

Mitigation: Proceed with auto-registration only after explicit user consent, or bypass it by configuring ZLBX_API_KEY or ~/.zlbx/config.json before use.

Risk: Generated HTML reports can contain signed bid or company links that may grant access without a separate login.

Mitigation: Review generated reports before sharing, and remove or redact signed sk links when forwarding outside the intended team.

Risk: Bid recommendations may be incomplete or misleading when public procurement data is missing, stale, or not matched to the user's project.

Mitigation: Require the report to call out data gaps, separate facts from inferences, and keep final bid/no-bid decisions under human review.

Risk: Reports are written to disk by default and may contain project, buyer, competitor, and pricing details.

Mitigation: Check the absolute report path, control file access, and delete or move generated reports according to the user's data-handling policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Quick Reference](references/api-quick.md)
- [Five-Step Bid Decision Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s77)
- [Zhiliaobiaoxun Business Portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or consent-based auto-registration; full reports typically use 12-25 data queries and quick assessments use 5-8 queries.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
