## Description:

Produces bid-and-tender-based company intelligence reports covering company profiles, business focus, customer and supplier relationships, win history, competitors, public risk signals, and optional contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, procurement, and competitive-intelligence users provide one or two company names to generate a bid-and-tender-based due-diligence report. The skill helps compare companies, summarize bidding strength, identify real competitors from bid overlap, and present reportable evidence with data boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, regions, and related query terms are sent to Zhiliaobiaoxun services for report generation.

Mitigation: Use the skill only when that data sharing is acceptable and avoid submitting sensitive local files or unrelated confidential material.

Risk: Consent-gated trial registration may transmit a MAC-derived device hash for duplicate-trial prevention.

Mitigation: Prefer a manually configured ZLBX_API_KEY when possible, and proceed with automatic registration only after explicit user consent.

Risk: The skill can store an API key in ~/.zlbx/config.json.

Mitigation: Protect local configuration files, avoid pasting credentials into chat, and rotate the key if it may have been exposed.

Risk: Generated reports may include signed platform links and cited company or bid records that are easy to share.

Mitigation: Review generated Markdown and HTML reports before sharing, especially when they include signed links, public-risk summaries, or contact data.

Risk: Optional contact lookup may return project contact data.

Mitigation: Use contact lookup only for legitimate business needs and do not try to reconstruct or bulk export masked contact details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha)
- [Publisher profile: dragonzu](https://clawhub.ai/user/dragonzu)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Report template reference](artifact/references/report-template.md)
- [Zhiliaobiaoxun API domain](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s124)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, optional self-contained HTML report files, concise user guidance, and background shell/API execution plans.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated trial registration; generated reports may contain signed platform links and cited company or bid records.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
