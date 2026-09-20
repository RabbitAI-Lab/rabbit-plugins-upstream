## Description:

AI-powered university course planning assistant that analyzes course catalogs, recommends courses based on student goals, generates optimized weekly schedules with enrollment priority markers, and exports Excel and ICS calendar files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

Students, advisors, and education teams use this skill to collect official course catalog information, plan semester course selections, build conflict-free timetables, and export schedules for review or calendar use. Local mode supports a single student and school, while the paid cloud mode supports batch or institutional planning with standardized decision reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private planning data may be sent to a paid cloud provider when cloud mode is selected.

Mitigation: Use local mode for private or single-student planning; before each paid cloud run, confirm the provider, endpoint, fee, and exact fields being sent.

Risk: Cloud tokens or API keys could be exposed if pasted into a chat or shared workspace.

Mitigation: Never paste LoomLoom tokens into chat; use interactive login or secure local environment storage, and install optional CLI tooling only from reviewed releases with checksum verification.

Risk: Course, timetable, or recommendation outputs can be incomplete when the submitted catalog lacks official source data.

Mitigation: Collect official catalog and timetable text before cloud submission, run the bundled validation and anti-hallucination checks, and mark missing or default schedule data before presenting results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [Project homepage](https://github.com/ez-hq/uni-course-scheduler)
- [Catalog Collection](references/catalog-collection.md)
- [Interaction Flow](references/interaction-flow.md)
- [Cloud Output Format](references/cloud-output-format.md)
- [Excel Output Specification](references/excel-output-spec.md)
- [Local Validation Contract](references/local-validation.md)
- [LoomLoom Cloud Execution Guide](references/loomloom-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Conversational guidance with markdown reports, JSON schedule data, shell commands, Excel workbooks, and ICS calendar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud mode requires explicit provider, endpoint, fee, and data-disclosure confirmation before each paid run; local mode keeps planning data local for single-student use.]

## Skill Version(s):

2.7.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
