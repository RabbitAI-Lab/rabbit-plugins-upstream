## Description:

This skill helps agents analyze medical-device and hospital procurement bids using Zhiliaobiaoxun tender data to assess whether to bid, likely competitors, pricing anchors, and reporting risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to evaluate a specific hospital or medical-device procurement opportunity, estimate competition and pricing, and produce a bid decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive procurement plans and bid strategy context.

Mitigation: Use it only for information you are authorized to process, and review generated recommendations before relying on them for commercial decisions.

Risk: The skill can perform automatic account registration, store credentials locally, and use device fingerprinting for trial-account deduplication.

Mitigation: Prefer a managed ZLBX_API_KEY, require explicit user consent before auto-registration, and review ~/.zlbx/config.json for stored credentials.

Risk: Generated reports and signed links may be shareable outside the intended audience.

Mitigation: Avoid publishing generated reports or signed links publicly, and check ~/zlbx-bid-decision-files/ for files that should be restricted or removed.

Risk: Bid analysis may be incomplete or misleading when source data is missing, stale, or ambiguous.

Mitigation: Validate key figures, company names, source citations, and data gaps before acting on the report.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/medical-device-bid-decision)
- [API Quick Reference](artifact/references/api-quick.md)
- [Five-Step Analysis Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration Flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun Agent Platform](https://agent.zhiliaobiaoxun.com)
- [Zhiliaobiaoxun Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report plus optional HTML report file generated from JSON input.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform API calls, consume account credits, and create local HTML reports under ~/zlbx-bid-decision-files/.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
