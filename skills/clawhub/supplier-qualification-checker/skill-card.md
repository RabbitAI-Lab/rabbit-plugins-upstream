## Description:

Helps procurement, bidding, contractor, and owner-side users check supplier qualifications, delivery capability, performance history, cooperation evidence, and public risk signals using Zhiliaobiaoxun bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, tendering organizations, general contractors, and owner-side users use this skill to produce a supplier due-diligence report for one company or a side-by-side comparison of two candidate suppliers. The report focuses on public bidding records, customer and supplier relationships, winning-bid strength, competitor overlap, and cited public risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and use a vendor API key locally during account setup.

Mitigation: Review the account flow before installation and prefer a manually managed ZLBX_API_KEY when automatic registration is not desired.

Risk: Automatic registration can collect a hashed MAC-derived device identifier for free-trial deduplication.

Mitigation: Use a preconfigured API key to bypass automatic registration if device-derived registration metadata is not acceptable.

Risk: Generated reports can include signed access links and are written to disk by default.

Mitigation: Share generated reports and signed links only with intended recipients and review local report storage before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker)
- [API quick reference](artifact/references/api-quick.md)
- [Seven-step workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun skill docs](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliaobiaoxun agent platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown supplier due-diligence report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company and two-company comparison modes; cited report evidence is limited and summarized to avoid overexposure.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
