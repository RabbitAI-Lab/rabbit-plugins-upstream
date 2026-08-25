## Description:

商机雷达 helps agents find early business opportunities from proposed projects, purchase intentions, and expiring renewal windows, then rank them by value and provide next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development, sales, and market-research users use this skill to scan a product, industry, or region for early opportunity leads before formal tender publication. The skill produces a prioritized opportunity list with objective data, gaps, and recommended follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags automatic account creation after consent and use of a hashed MAC-derived device identifier for free-trial deduplication.

Mitigation: Pre-set ZLBX_API_KEY to skip auto-registration, and only allow registration after reviewing the consent prompt and device-feature disclosure.

Risk: The skill may persist an API key in ~/.zlbx/config.json.

Mitigation: Prefer environment-based credential provisioning for managed deployments, restrict local config file access, and remove the stored key when the skill is no longer used.

Risk: Generated local HTML reports can contain opportunity details and are written under ~/zlbx-opportunity-radar-files/.

Mitigation: Review report contents before sharing, delete stale reports when no longer needed, and avoid exporting contact information unless explicitly required.

Risk: Recharge or login links are part of the account workflow.

Mitigation: Review links before use and confirm they resolve to the expected zhiliaobiaoxun.com domains.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliao opportunity platform](https://agent.zhiliaobiaoxun.com)
- [Zhiliao API endpoint family](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown opportunity report with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for API access; full scans estimate 8-15 calls and optional HTML reports are written under ~/zlbx-opportunity-radar-files/.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
