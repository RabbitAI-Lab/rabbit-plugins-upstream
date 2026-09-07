## Description:

This skill helps agents discover early tender opportunities by scanning proposed projects, purchase intentions, and expiring contracts, then ranking opportunities by value and readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and bidding teams use this skill to find early procurement leads for a product, industry, or region before tenders are formally released. Agents can return ranked opportunity lists, follow-up actions, and optional shareable HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor may receive tender search terms and, during automatic registration, platform, CPU architecture, and a hashed MAC address for trial deduplication.

Mitigation: Prefer supplying an existing ZLBX_API_KEY; require user consent before automatic registration; disclose the three collected device attributes before registration.

Risk: The skill can store credentials locally and produce direct-access or auto-login links that should not be exposed broadly.

Mitigation: Protect ~/.zlbx/config.json, avoid sharing API keys or signed report links in chats, and review reports before forwarding them.

Risk: Scheduled scans can repeat external API calls and consume account credits.

Mitigation: Tell users the expected credit cost before scans, keep default call budgets bounded, and review any recurring scan configuration.

Risk: Tender opportunity data can be incomplete, delayed, or unsuitable as the sole basis for a commercial decision.

Mitigation: Keep rankings traceable to returned amount, date, status, and matching signals, and include a disclaimer that users should independently verify decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Opportunity workflow](references/workflow.md)
- [Auto-registration reference](references/auto-register.md)
- [Report template](references/report-template.md)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliaobiaoxun opportunity workspace](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML files, Shell commands, Configuration guidance]

**Output Format:** [Markdown opportunity lists with optional self-contained HTML reports and concise setup or follow-up guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based automatic registration; complete scans estimate 8-15 API calls and may write reports under ~/zlbx-opportunity-radar-files/.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
