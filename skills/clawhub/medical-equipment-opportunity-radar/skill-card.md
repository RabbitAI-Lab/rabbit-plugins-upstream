## Description:

Scans hospital construction projects, procurement intentions, and expiring service contracts to identify and prioritize early medical-equipment sales opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Medical-device sales teams and other external users provide a product line or region to find and rank prospective hospital purchases, with supporting public procurement signals and suggested follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account registration submits device features, including a hashed network identifier.

Mitigation: Review before installing and use a preconfigured ZLBX_API_KEY to avoid registration and device-feature submission.

Risk: The skill saves an API key and generated reports under the user's home directory.

Mitigation: Limit access to local credentials and reports, and remove them when no longer needed.

Risk: Reports and links may contain signed access or auto-login parameters.

Mitigation: Treat reports and signed links as sensitive; do not forward them publicly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/medical-equipment-opportunity-radar)
- [Scanning workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Account registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Prioritized Markdown opportunity list; optional self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, ranking reasons, data gaps, and suggested next actions.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
