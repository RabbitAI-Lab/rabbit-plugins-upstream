## Description:

Identifies sleep states like deep sleep, light sleep, waking, and restlessness, and generates daily sleep reports and schedule analysis to help parents understand a baby's sleep patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregiving workflows use this skill to analyze infant sleep-monitoring videos or video URLs, classify sleep states, retrieve cloud report history, and return structured sleep reports for parenting reference. The output should not be treated as medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Baby-monitoring videos or video URLs may be sent to the lifeemergence.com backend.

Mitigation: Use the skill only after explicit user confirmation, especially before processing real household or child footage.

Risk: The skill can create or reuse an internal account identity and query cloud report history.

Mitigation: Make the account and report-history behavior clear to users and provide a deletion or reset path before production use.

Risk: Reusable authentication tokens may be stored in a local workspace SQLite database.

Mitigation: Protect the workspace, restrict access to local data files, and define token deletion or rotation procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown and JSON text with report links, plus an optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; documented formats are mp4, avi, and mov up to 10 MB.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
