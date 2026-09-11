## Description:

Finds early IT project opportunities by scanning proposed projects, procurement intentions, and expiring contracts, then ranks results with follow-up suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and partner teams use this skill to turn an industry, product, or region query into a ranked list of early IT opportunities. It supports China-focused discovery across proposed projects, procurement intentions, and renewal windows, with suggested next actions for each opportunity.

### Deployment Geography for Use:

Global use; China-focused procurement and project data coverage.

## Known Risks and Mitigations:

Risk: The provider receives search terms used for opportunity discovery.

Mitigation: Review queries before use and avoid submitting confidential keywords or sensitive local context.

Risk: Automatic signup can collect a stable device identifier made from platform, CPU architecture, and a MAC-address hash.

Mitigation: Use a pre-created ZLBX_API_KEY to avoid automatic signup, or proceed only after reviewing and accepting the device identifier collection.

Risk: API credentials are stored locally and generated reports may contain signed detail or login-style links.

Mitigation: Protect ~/.zlbx/config.json, avoid sharing generated sk or auto-login links, and review generated HTML reports before distribution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](references/api-quick.md)
- [Opportunity Radar Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Automatic Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown opportunity report and optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ranked opportunities, source links, data notes, follow-up actions, and generated report file paths; may include signed detail links returned by the provider API.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
