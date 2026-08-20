## Description:

Finds early tender and procurement opportunities from proposed projects, purchase intents, and expiring contracts, then ranks them into an actionable opportunity list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and market research teams use this skill to discover early-stage tender opportunities for a product, industry, or region. It helps prioritize follow-up actions before formal bid publication or contract renewal windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration can collect device fingerprint data and create a vendor account when no API key is configured.

Mitigation: Set ZLBX_API_KEY manually when possible, and do not use auto-registration on sensitive machines.

Risk: Local credential storage may persist API credentials outside the skill directory.

Mitigation: Review local credential storage before installation and remove stored credentials when the skill is no longer needed.

Risk: Generated HTML reports and sk-bearing links can provide access to report or tender details if shared broadly.

Mitigation: Treat generated reports and signed links as private access material rather than public documents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [Workflow Reference](artifact/references/workflow.md)
- [API Quick Reference](artifact/references/api-quick.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown opportunity lists with optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY and may create local HTML reports containing signed links.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
