## Description:

This skill helps an agent evaluate a specific bidding opportunity with Zhiliaobiaoxun bid data, producing a decision report on whether to bid, likely competitors, pricing reference, buyer tendencies, and bid-failure risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, sales, and bidding teams use this agent skill to assess a concrete procurement opportunity before investing in a bid. It gathers and structures bid-history signals into a Markdown decision report and, in full mode, an optional shareable HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid-related search terms and company or project data are sent to Zhiliaobiaoxun services during analysis.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting confidential bid material unless the organization has approved the vendor and data flow.

Risk: Optional trial registration can transmit a MAC-derived device hash for device-level de-duplication.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when device fingerprinting is not acceptable, and require explicit user consent before any automatic registration step.

Risk: The skill stores an API key and generated reports on disk.

Mitigation: Protect local configuration and report directories, rotate or remove stored credentials when no longer needed, and avoid placing exported reports in shared locations by default.

Risk: Generated HTML reports and citations may include signed bid or company links.

Mitigation: Review reports before sharing and remove sensitive links or citations when signed URLs should not be exposed outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent)
- [API quick reference](artifact/references/api-quick.md)
- [Analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional generated HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration; full analyses are documented as consuming about 12-25 API calls, while lightweight analyses use about 5-8 calls.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
