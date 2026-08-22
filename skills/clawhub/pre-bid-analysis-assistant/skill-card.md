## Description:

This skill helps agents produce pre-bid due diligence reports that assess project fit, buyer history, likely competitors, pricing references, risks, and bid/no-bid recommendations from bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External commercial, sales, bid, and procurement teams use this skill to evaluate whether to pursue a specific tender, how to price, and which competitors or red flags require attention before bidding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential persistence and API key use may expose account access if local configuration or generated outputs are mishandled.

Mitigation: Prefer a manually created API key stored in ZLBX_API_KEY, avoid placing credentials in chat or reports, and rotate the key if exposure is suspected.

Risk: Auto-registration collects device-derived identifiers for trial-account de-duplication.

Mitigation: Preconfigure ZLBX_API_KEY to skip auto-registration, or require explicit user consent before any registration request.

Risk: Shareable HTML reports may preserve signed detail-page links and local report contents.

Mitigation: Review generated reports before sharing and distribute them only to recipients authorized to see the tender details and signed links.

Risk: Bid recommendations and competitor assessments may affect commercial decisions or reputations.

Mitigation: Verify cited data, keep facts separate from inferred signals, and use human review before relying on the report for a bid decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant)
- [Workflow](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown report in chat and optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; full reports typically use 12-25 data queries and may include API-returned signed detail links.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
