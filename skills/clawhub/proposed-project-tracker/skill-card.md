## Description:

Tracks early-stage proposed projects, procurement intentions, and expiring contracts so users can discover and prioritize business opportunities before formal tender announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development and sales users use this skill to scan Zhiliaobiaoxun project and bidding data for early opportunity leads, rank them by amount, maturity, urgency, and keyword fit, and produce shareable opportunity reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or reuse a local provider account and persist an API key in ~/.zlbx/config.json.

Mitigation: Prefer preconfiguring ZLBX_API_KEY, review ~/.zlbx/config.json after use, and remove stored credentials when the skill is no longer needed.

Risk: Auto-registration collects platform, CPU architecture, and a hashed MAC address for device deduplication.

Mitigation: Use a manually provided ZLBX_API_KEY to bypass auto-registration, and only approve registration after reviewing the provider's device-data disclosure.

Risk: Generated Markdown and HTML reports may include sk-bearing links that grant access without a normal login prompt.

Mitigation: Treat generated reports and copied links as shareable access artifacts; do not forward them outside the intended audience.

Risk: Opportunity rankings and business recommendations rely on provider API data that may be incomplete or delayed.

Mitigation: Use the reports as lead discovery, preserve the skill's disclaimers, and independently verify important project, budget, and contact details before action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/proposed-project-tracker)
- [API Quick Reference](references/api-quick.md)
- [Workflow Guide](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name})
- [Zhiliaobiaoxun Opportunity Platform](https://agent.zhiliaobiaoxun.com)
- [Zhiliaobiaoxun AI Open Platform](https://ai.zhiliaobiaoxun.com/?ch=s98)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists and optional HTML report files generated from JSON report data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a consent-gated auto-registration flow; reports may include signed sk access links returned by the provider API.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
