## Description:

AI销售线索雷达 helps government and enterprise sales, BD, and channel teams find and rank early sales opportunities from proposed projects, procurement intents, and expiring contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, BD, and channel users use this skill to scan for potential customers and prioritize opportunities by value, timing, maturity, and product fit. It produces concise opportunity lists and optional HTML reports from vendor procurement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sales search terms to a third-party procurement API and may create accounts or store returned API keys locally.

Mitigation: Prefer configuring a user-provided ZLBX_API_KEY, review ~/.zlbx/config.json permissions after use, and approve automatic registration only when the vendor data flow is acceptable.

Risk: Optional auto-registration transmits a stable MAC-derived device hash for free-trial deduplication.

Mitigation: Skip auto-registration by preconfiguring ZLBX_API_KEY or a local config file, and disclose the device-feature collection before registration.

Risk: Generated reports and source links may contain login-bearing or signed links that should not be broadly shared.

Mitigation: Share reports only with intended recipients and avoid reposting sk or SID links in public channels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar)
- [API Quick Reference](references/api-quick.md)
- [Workflow Guide](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity reports, optional self-contained HTML report files, and concise configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or a local ~/.zlbx/config.json API key; full scans disclose expected credit use before querying.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
