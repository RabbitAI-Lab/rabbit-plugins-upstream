## Description:

Matches a pet from an image or video to vaccination records and reports whether a dose is due or overdue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet hospital and boarding staff can use the skill to compare a pet's linked vaccination records with the reminder interval and retrieve past reports. Its results are record comparisons, not veterinary advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload media for remote processing despite a no-analysis option.

Mitigation: Confirm authorization before sending private clinic media, obtain the provider's retention and deletion terms, and do not rely on --api-url to change the destination.

Risk: The skill manages accounts and credentials without adequate user control.

Mitigation: Confirm authorization for account creation and protect the workspace account database.

Risk: Reminder results depend on the linked vaccination records.

Mitigation: Verify results against clinic records; treat them as database comparisons rather than veterinary advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured vaccination reminder report in JSON or text, with optional Markdown history table and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Due or overdue status based on linked vaccination records; report links when available]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
