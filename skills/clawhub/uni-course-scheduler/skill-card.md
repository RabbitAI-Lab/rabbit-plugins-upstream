## Description:

Helps university students choose courses, build weekly timetables, and export Excel workbooks and calendar files from course-catalog information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

Students and academic advisers use this skill to review university course catalogs, recommend courses around student goals and prerequisites, plan weekly schedules, and export planning files. Institutions can opt into a paid cloud mode for batch planning and a standardized decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud mode sends course catalog and planning details to a selected external service and may incur a fee.

Mitigation: Disclose the destination, submitted details, and fee; obtain explicit confirmation before each submission.

Risk: Credentials could be exposed if pasted into chat.

Mitigation: Use interactive login for tokens and never request API keys in chat.

Risk: Incorrect catalog information or timezone settings could produce unreliable schedules and calendar entries.

Mitigation: Check critical courses against official sources, confirm the timezone, and review generated schedules before relying on them.

Risk: Locally generated workbooks and calendars may contain sensitive student planning details.

Mitigation: Review local files before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [Declared project homepage](https://github.com/ez-hq/uni-course-scheduler)
- [Catalog collection](references/catalog-collection.md)
- [Local validation](references/local-validation.md)
- [Cloud output format](references/cloud-output-format.md)
- [Excel output specification](references/excel-output-spec.md)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Course recommendations and weekly schedule in text; Excel (.xlsx) workbook and calendar (.ics) file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local mode supports one school and one student; paid cloud mode supports batch planning and a standardized decision report.]

## Skill Version(s):

2.7.10 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
