## Description:

Yance Report Gen synthesizes role-specific investment analysis JSON files into a unified markdown research report.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to combine at least four role-specific JSON analysis reports into a single teaching-oriented investment research report. The generated report is for course demonstration only and is not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated investment research content could be mistaken for financial advice.

Mitigation: Use the skill only for course demonstration, preserve the report disclaimer, and require human review before relying on any generated conclusion.

Risk: Missing or incomplete role JSON inputs can produce placeholder report sections.

Mitigation: Provide the expected yanmu, yanlin, yanji, yansheng, and yandun JSON inputs where available, and check generated sections marked as demonstration placeholders.

Risk: The script writes a markdown report to the selected output directory.

Mitigation: Use a dedicated output folder to avoid writing the generated report into an unintended location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yance-report-gen)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown report written to a dated .md file, with optional JSON status printed by the script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads user-supplied JSON role reports and writes output to the selected directory.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
