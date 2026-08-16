## Description:

AI销售线索雷达 helps government and enterprise sales, BD, and channel teams find and prioritize sales leads from proposed projects, purchase intentions, expiring contracts, and recurring lead reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales and business-development users use this skill to scan public procurement and project signals for government and enterprise opportunities, rank leads by value and urgency, and generate lead lists or scheduled morning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports and copied opportunity links may contain login-bypass sk parameters.

Mitigation: Avoid broad sharing of generated reports or links, and review report contents before distribution.

Risk: The skill handles local API credentials and can create files under ~/.zlbx/ and ~/zlbx-opportunity-radar-files/.

Mitigation: Prefer a user-provided ZLBX_API_KEY when available and review local credential and report files after installation or use.

Risk: Automatic trial registration sends search-service account data and a hashed MAC-derived device identifier to Zhiliaobiaoxun after user approval.

Mitigation: Use automatic registration only after informed consent, or configure ZLBX_API_KEY manually to skip the registration flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, files, shell commands, guidance]

**Output Format:** [Markdown lead lists with optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic trial registration; reports may include API-returned signed links.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
