## Description:

Generates bid-data-based company intelligence reports covering business profile, customer and supplier relationships, tender-winning strength, competitors, public risk signals, and optional company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to investigate a named company from a Chinese public procurement and bidding-data perspective. It helps produce single-company due diligence reports or two-company comparisons with cited data boundaries, cost estimates, and optional shareable HTML output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names and query terms are sent to Zhiliaobiaoxun APIs, and usage depends on its account and credit system.

Mitigation: Install only when that data sharing is acceptable, and inform users of estimated credit consumption before running a report.

Risk: Automatic registration can collect a device identifier and store an API key locally.

Mitigation: Prefer a user-provided ZLBX_API_KEY; if no key exists, get explicit user consent before registration and verify local permissions on ~/.zlbx/config.json.

Risk: Generated HTML reports can contain signed company or bid links and contact details that are suitable only for the intended audience.

Mitigation: Review generated reports before sharing, preserve API-returned link semantics, and avoid sharing signed links or contact information beyond the intended recipients.

Risk: Public company risk sections can affect real organizations if phrased as unsupported allegations.

Mitigation: Use only sourced, factual language for public risk signals, separate facts from inference, and include data-boundary disclaimers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-intel-qichamao)
- [API Quick Reference](references/api-quick.md)
- [Company Intelligence Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Account and Registration API](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation, plus optional self-contained HTML report file generated from structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; API-returned company and bid links may include signed access parameters and should be handled as shareable links.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
