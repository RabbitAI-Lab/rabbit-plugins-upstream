## Description:

This skill helps bidding teams investigate competitors from a tendering perspective, using ZLBX bidding data to produce traceable competitor, customer, contract, risk, and company-comparison intelligence reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, bidding, procurement, and competitive-intelligence users use this skill to research a named company, assess bidding strength and customer relationships, identify real competitors from tender overlap, and compare two companies before bid or supplier decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML reports and platform URLs can include signed sk parameters that bypass login for linked company or announcement pages.

Mitigation: Treat generated reports and signed links as sensitive; share them only with trusted recipients and avoid posting them publicly.

Risk: The skill can persist a ZLBX API key in ~/.zlbx/config.json and uses ZLBX_API_KEY when configured.

Mitigation: Protect local credential files, do not paste API keys into chat, and prefer managed environment variables where available.

Risk: Optional auto-registration may collect platform, CPU architecture, and a hashed MAC address after user consent.

Mitigation: Require explicit consent before auto-registration and preconfigure ZLBX_API_KEY to bypass auto-registration entirely.

Risk: Company names, search terms, and bidding-analysis queries are sent to the ZLBX service for research.

Mitigation: Use the skill only when sending those business queries to ZLBX is acceptable, and avoid entering confidential unreleased bid strategy details.

Risk: Competitor and public-risk reports can affect real commercial decisions and may rely on incomplete public bidding data.

Mitigation: Review conclusions against source links, preserve data-boundary notes, and use the report as decision support rather than a final determination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](artifact/references/api-quick.md)
- [Seven-step workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [ZLBX company intelligence platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown competitor-intelligence report, optional self-contained HTML report file, and guidance for API-backed follow-up analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; reports may be saved under ~/zlbx-company-intel-files/ and may contain signed sk links.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
