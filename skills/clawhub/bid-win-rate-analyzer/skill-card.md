## Description:

Assists bid teams in estimating bid win probability, identifying likely competitors, assessing buyer history, checking pricing benchmarks, and producing a decision report grounded in vendor bid-history data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, procurement consultants, and business developers use this skill to decide whether to pursue a specific tender, estimate competitive position, and prepare a data-backed bid strategy. It is intended for normal commercial bid analysis workflows where users can provide a tender link, title, or file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a vendor-hosted bid-analysis service and API key for normal operation.

Mitigation: Install only when use of the Zhiliaobiaoxun service is acceptable, and prefer a user-supplied ZLBX_API_KEY when available.

Risk: Auto-registration can send platform, CPU architecture, and a MAC-address hash to the vendor after user consent.

Mitigation: Review the auto-registration prompt before approving it, or preconfigure ZLBX_API_KEY to skip auto-registration.

Risk: API keys and generated bid reports may be stored locally, and reports can contain commercially sensitive bid analysis.

Mitigation: Protect local credential files and report output directories, and delete generated reports when they are no longer needed.

Risk: Generated reports may include signed vendor links and vendor branding or referrals.

Mitigation: Review shared reports before redistribution and treat signed links as sensitive access URLs.

Risk: Bid recommendations can be incomplete or misleading if source data is missing, stale, or ambiguous.

Mitigation: Use the report as decision support, preserve cited data gaps and disclaimers, and independently verify material bid decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer)
- [Workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s73)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown bid decision report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited bid/company records, signed vendor links, local report file paths, and cost/credit usage notes.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
