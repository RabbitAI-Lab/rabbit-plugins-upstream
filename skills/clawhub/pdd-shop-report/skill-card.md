## Description:

Generates single-shop HTML reports and multi-shop dashboards for Pinduoduo merchants from previously synced shop data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

Pinduoduo merchants and their operations teams use the skill to review sales, orders, inventory health, and action items across one or more shops after syncing their data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An optional remote ClickHouse connection can send or query merchant data at a configured URL; the manifest does not fully disclose that external data flow.

Mitigation: Leave PDD_CH_URL unset unless using a trusted, controlled ClickHouse endpoint, preferably over HTTPS.

Risk: Generating a report can overwrite the selected HTML output file.

Mitigation: Review and choose the report output path before running.

## Reference(s):

- [PDD Shop Report on ClawHub](https://clawhub.ai/claw-school/skills/pdd-shop-report)
- [Claw School](https://claw-school.com)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands]

**Output Format:** [JSON status response and standalone HTML report with embedded charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-shop and multi-shop views; requires previously synced shop data.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
