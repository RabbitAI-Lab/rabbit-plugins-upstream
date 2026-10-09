## Description:

Queries Ozon China-zone product sales rankings by category, period, sales, revenue, and price for cross-border product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and analysts use this skill to find and compare Ozon products sold through the China zone, filtering rankings by category, time period, sales, revenue, or price. Queries use a paid Qinghu data service and require user approval before charges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install unpinned external tooling or change the local environment.

Mitigation: Review the package first and use platform-managed, version-pinned installation rather than allowing automatic setup during a query.

Risk: Queries can incur charges and require a locally configured API token.

Mitigation: Use a trusted token configuration and obtain user approval for estimated charges before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-china-zone-products)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise narrative and tabular previews; spreadsheet files for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include platform and time-period context; paid queries report credits used.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
