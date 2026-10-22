## Description:

Analyzes university course catalogs, recommends courses based on student goals, builds weekly schedules, and exports Excel workbooks and ICS calendars for local or optional paid cloud planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

University students use the skill to review course catalogs, plan courses around degree requirements and personal preferences, and create a weekly timetable. Local planning is available for one student at one school; optional paid cloud planning supports batch and institutional workflows.

### Deployment Geography for Use:

Global; supports US, Australian, UK, Chinese, and ECTS-based education systems.

## Known Risks and Mitigations:

Risk: Automated recommendations and schedules may be inaccurate even when validation checks pass.

Mitigation: Verify course requirements and meeting times with the university before relying on the plan.

Risk: Optional paid cloud use transfers planning inputs to a provider and incurs fees.

Mitigation: Prefer local mode when suitable; otherwise review provider privacy and retention terms, minimize student data, and approve the data and cost before cloud use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [Project homepage (declared in skill metadata)](https://github.com/ez-hq/uni-course-scheduler)
- [Catalog collection guidance](references/catalog-collection.md)
- [Excel output specification](references/excel-output-spec.md)
- [Cloud setup and usage guidance](references/loomloom-setup.md)

## Skill Output:

**Output Type(s):** [Text, Spreadsheet file (.xlsx), Calendar file (.ics)]

**Output Format:** [XLSX workbook, ICS calendar, and textual planning summary; cloud mode can also provide a decision report and degree-audit workbook sheet.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on mode: local planning is for one student at one school; optional paid cloud planning supports batch workflows and requires explicit fee confirmation.]

## Skill Version(s):

2.7.11 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
