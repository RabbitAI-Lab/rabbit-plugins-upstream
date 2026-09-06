## Description:

Offer Tracker organizes Chinese campus recruiting and internship application updates from free-form chat entries into a browser-based HTML progress table with a JSON backup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn batches of Chinese recruiting and internship application notes into a searchable local tracker, update application statuses, maintain a JSON backup, and report upcoming deadlines or interviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tracker can contain job-application data in a local Desktop HTML file, browser storage, and JSON backup.

Mitigation: Store only the application details needed for tracking, and avoid passwords, verification codes, application numbers, or unrelated personal information.

Risk: The JSON backup is overwritten with the latest full record set during normal use.

Mitigation: Review the target tracker and backup before updates, and keep a current full backup for recovery or browser merge import.

## Reference(s):

- [Input Parsing Rules](references/parsing-rules.md)
- [ClawHub Skill Page](https://clawhub.ai/sharinchan233/skills/offer-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown status summaries with local HTML and JSON file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a browser-openable HTML tracker and a full-record JSON backup for merge import and recovery.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
