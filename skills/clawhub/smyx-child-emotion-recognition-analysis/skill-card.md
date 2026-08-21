## Description:

Analyzes child surveillance images or videos to identify negative emotions such as crying, anger, fear, and distress, then returns structured reports, reminders, notifications, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, parents, daycare operators, and developers use this skill to analyze uploaded or URL-based child images and videos for emotion signals and to retrieve historical cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload child images or videos to LifeEmergence services.

Mitigation: Use only with guardian and operator consent, and confirm retention, deletion, and notification-recipient expectations before deployment.

Risk: The skill may create or reuse an internal account identity and store tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace, protect the local database, avoid shared machines, and rotate or revoke credentials if the workspace is exposed.

Risk: The skill can retrieve prior cloud reports for sensitive child surveillance analysis.

Mitigation: Limit historical-report access to authorized users and verify the account context before running report-list queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Child emotion recognition API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown text with JSON-formatted structured analysis or report-list content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include LifeEmergence report export links; results can optionally be written to a user-specified output file.]

## Skill Version(s):

1.0.22 (source: ClawHub release evidence; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
