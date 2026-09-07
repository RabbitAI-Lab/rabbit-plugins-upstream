## Description:

Uni Course Scheduler helps agents analyze university catalogs, recommend courses, build conflict-free weekly timetables, and export Excel workbooks and ICS calendars for local or paid cloud workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

External students, advisors, and education teams use this skill to turn official course catalog text and student preferences into course recommendations, weekly schedules, enrollment-priority notes, and calendar or workbook outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cloud mode can send university, program, catalog text, and user-provided planning details to a paid external service.

Mitigation: Review the fields being sent, confirm the selected LoomLoom endpoint and fee before each submission, and use local mode when external submission is not appropriate.

Risk: Optional cloud tooling introduces supply-chain exposure during installation.

Mitigation: Use a virtual environment, pin package versions with hashes where possible, and verify the LoomLoom release tag and checksum before installing extras.

Risk: Incomplete or stale catalog and timetable data can produce missing or low-confidence course plans.

Mitigation: Collect official catalog text, apply the documented quality gates, and run the included validation and anti-hallucination checks before relying on outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [Project Homepage](https://github.com/ez-hq/uni-course-scheduler)
- [Catalog Collection](references/catalog-collection.md)
- [Cloud Output Format](references/cloud-output-format.md)
- [Excel Output Specification](references/excel-output-spec.md)
- [Interaction Flow](references/interaction-flow.md)
- [Local Validation Contract](references/local-validation.md)
- [LoomLoom Cloud Execution Guide](references/loomloom-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with JSON inputs and generated Excel workbook or ICS calendar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local mode produces a 6-sheet Excel workbook and textual schedule overview; cloud mode can add a decision report, degree audit, and downloadable ICS calendar after user confirmation.]

## Skill Version(s):

2.7.6 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
