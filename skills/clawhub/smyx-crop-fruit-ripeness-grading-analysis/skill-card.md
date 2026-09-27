## Description:

Grades the ripeness of crop fruits from images or videos using visual features and returns a report to support harvest timing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisors use fruit images or videos to assess ripeness stages, review harvest guidance, and retrieve past grading reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fruit images and videos are uploaded to a cloud analysis service, and report history can be queried remotely.

Mitigation: Obtain permission before uploading media, avoid sensitive imagery, and review the service's data handling before use.

Risk: The skill may silently create or reuse an account, log in remotely, and store session tokens in a local SQLite database without clear inspection or deletion controls.

Mitigation: Review the account and session model before installation; restrict access to the workspace and arrange separate credential and account cleanup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis)
- [Skill API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured grading report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include harvest guidance and report links; results can optionally be saved to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
