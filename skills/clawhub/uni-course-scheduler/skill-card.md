## Description:

AI-powered university course planning assistant that analyzes official course catalogs, recommends courses based on student goals, generates conflict-free weekly schedules with enrollment priority markers, and exports Excel and ICS calendar files across multiple international credit systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

LicenseRef-Personal-Use

## Use Case:

Students, education advisors, and institution-facing agents use this skill to plan university course selections, compare requirements, build weekly timetables, and create exportable schedule artifacts. It supports local single-student planning and paid cloud workflow routing for batch or decision-report use cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports unsafe token-pasting setup guidance for live API keys.

Mitigation: Configure LoomLoom tokens only through local environment variables or a secret manager; do not paste live tokens into prompts or chat messages.

Risk: The package includes an unrelated GitHub download-count script that reads GitHub credentials and calls the GitHub API.

Mitigation: Do not run scripts/check_github_downloads.py unless it has been reviewed for the deployment environment; remove or isolate it from normal skill execution.

Risk: Cloud scheduling depends on pre-collected catalog and timetable text, and incomplete inputs can produce missing or placeholder schedule data.

Mitigation: Collect official catalog and timetable sources before paid cloud runs, apply the documented quality gates, and validate generated workbooks before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ez-hq/skills/uni-course-scheduler)
- [Publisher profile](https://clawhub.ai/user/ez-hq)
- [Catalog collection guide](artifact/references/catalog-collection.md)
- [Cloud output format](artifact/references/cloud-output-format.md)
- [Excel output specification](artifact/references/excel-output-spec.md)
- [Interaction flow](artifact/references/interaction-flow.md)
- [Local validation contract](artifact/references/local-validation.md)
- [LoomLoom setup guide](artifact/references/loomloom-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Guided conversation, validation notes, shell commands, JSON-derived Excel workbooks, and ICS calendar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate a 6-sheet local Excel workbook, a 7-sheet cloud workbook with degree audit, and an ICS calendar when cloud schedule data is available.]

## Skill Version(s):

2.6.0 (source: frontmatter, skill.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
