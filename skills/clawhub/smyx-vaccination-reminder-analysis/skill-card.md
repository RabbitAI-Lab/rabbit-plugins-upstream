## Description:

Triggers when a user provides a pet facial image or video URL/file to identify the pet, check linked vaccination records, and report whether a dose is due or overdue; it does not provide medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet hospital teams, boarding staff, and pet insurers can use the skill to identify a pet from an image or video and check linked vaccination records for due or overdue reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles pet images or video and linked vaccination records through an external analysis service; account and report-history handling is not clarified in the supplied security guidance.

Mitigation: Before use, clarify the service's data handling and confirm that sending the media and related record data is acceptable; avoid sending media until this is resolved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON analysis results and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports vaccination status from linked records and may include a report link.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata; artifact frontmatter says 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
