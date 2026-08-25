## Description:

AI-powered university course planning assistant that analyzes official course catalogs, recommends courses from student goals, builds weekly timetables, and exports Excel workbooks plus cloud-mode ICS calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

LicenseRef-Personal-Use

## Use Case:

Students, advisors, and education-support agents use this skill to plan university coursework from official catalog data, compare recommended courses against student goals, and produce weekly schedules with exportable planning files. Cloud mode supports batch or institutional workflows after user confirmation, while local mode is positioned for single-student personal planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud mode sends course catalog text, student goals, and scheduling context to LoomLoom and may incur a fee.

Mitigation: Confirm cloud submission and fee estimates in conversation before running, and avoid including student IDs or unnecessary personal identifiers.

Risk: API tokens or platform keys could be exposed if pasted into chat.

Mitigation: Use interactive login or local environment variables, never paste tokens into the agent conversation, and rotate any token that was exposed.

Risk: Incomplete or unofficial catalog data can produce missing, default, or misleading timetable results.

Mitigation: Collect official catalog and timetable sources first, mark missing fields as NOT_FOUND or default_timetable where applicable, and run the included audit and schedule-validation scripts before relying on outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [ClawHub publisher profile](https://clawhub.ai/user/ez-hq)
- [Project homepage](https://github.com/ez-hq/uni-course-scheduler)
- [README](README.md)
- [Catalog Collection](references/catalog-collection.md)
- [Cloud Output Format](references/cloud-output-format.md)
- [Excel Output Specification](references/excel-output-spec.md)
- [Interaction Flow](references/interaction-flow.md)
- [Local Validation Contract](references/local-validation.md)
- [LoomLoom Cloud Execution Guide](references/loomloom-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Conversational guidance with JSON inputs, Markdown validation reports, Excel workbooks, and ICS calendar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Excel export is available in local and cloud modes; ICS calendar export is documented for cloud standard mode only.]

## Skill Version(s):

2.6.5-en (source: frontmatter, skill.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
