## Description:

Helps users assess bid win probability, pricing posture, likely competitors, buyer history, and key participation risks for a specific procurement opportunity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to decide whether to pursue a specific bid and to prepare a data-grounded decision report. The skill supports buyer profiling, competitor prediction, price benchmarking, fit analysis, and risk review using the vendor's procurement data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement search terms and project details are sent to the vendor service.

Mitigation: Install only when this data sharing is acceptable for the intended procurement workflow.

Risk: Auto-registration uses a MAC-derived device hash for trial-account deduplication.

Mitigation: Prefer manually setting ZLBX_API_KEY when users want to avoid auto-registration device fingerprinting.

Risk: The skill persists credentials and generated reports locally.

Mitigation: Review permissions for ~/.zlbx/config.json and the report output directory before broad deployment.

Risk: Generated HTML reports may contain signed sk links returned by the API.

Mitigation: Avoid broadly sharing generated reports unless the recipient should have access to those linked records.

Risk: Bid recommendations can be incorrect or incomplete when source data is incomplete or delayed.

Mitigation: Treat reports as decision support and require human review before commercial action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Quick Reference](artifact/references/api-quick.md)
- [Bid Analysis Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Workflow](artifact/references/auto-register.md)
- [ZLBX API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX AI Open Platform](https://ai.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report and supporting JSON for report rendering.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite data gaps, source time ranges, and API-derived evidence; generated HTML reports may include signed source links returned by the API.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
