## Description:

Coordinates Excel data analysis workflows for reading multi-sheet files, gating large-file handling, cleaning and filtering data, aggregating across sheets, visualizing results, and exporting Excel or CSV reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to guide agents through Chinese-language Excel analysis tasks, including row counting, schema inspection, cleaning, filtering, statistics, visualization, and report export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create local derived report files that overwrite or expose sensitive spreadsheet data.

Mitigation: Confirm output paths, avoid overwriting existing files, and use approved storage before exporting sensitive results.

Risk: Some text-cleaning examples retain only Chinese characters and can destructively remove other content.

Mitigation: Preview cleaning rules on a sample and confirm language assumptions before applying them to full datasets.

Risk: The skill broadly routes generic data-analysis requests into an Excel-focused workflow.

Mitigation: Use it only for spreadsheet analysis, cleaning, statistics, visualization, and export tasks that match the release scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-da-excel-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python code blocks, file export paths, and download-link text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local Excel, CSV, Parquet, image, and report files during agent-guided analysis.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
