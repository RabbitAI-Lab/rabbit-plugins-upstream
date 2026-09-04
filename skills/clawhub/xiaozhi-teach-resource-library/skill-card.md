## Description:

A Chinese-language resource library skill that helps independent teachers store, tag, search, adapt, and reuse handouts, questions, review scripts, and de-identified error cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to maintain a searchable teaching-resource library, retrieve resources by knowledge point and difficulty, adapt materials for a student context, and record reuse notes. It is intended for teacher-facing resource management, not direct student delivery, grading, lesson generation, or parent contact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student cases or resource notes could expose identifiable student information.

Mitigation: De-identify cases before saving them, avoid real names, school names, contact details, addresses, and uniquely identifying context, and honor deletion requests by reviewing related case entries.

Risk: Copyrighted teaching materials could be copied into the library without authorization.

Mitigation: Record a copyrightStatus for every resource and keep teaching-aid originals, exam papers, scans, and unauthorized reposts as indexes only instead of storing full content.

Risk: AI-generated questions may contain errors, ambiguous answers, unsuitable difficulty, or invalid conditions.

Mitigation: Mark AI-generated questions as aiGenerated and keep them out of student-facing use until a teacher verifies each item and sets verifiedByTeacher to true.

Risk: Built-in crisis contacts may not fit users outside Mainland China.

Mitigation: Replace listed emergency and mental-health contacts with local crisis resources before relying on them in another region.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization, search, and de-identification](references/resource-categorization.md)
- [Resource entry examples](references/resource-entry-examples.md)
- [Copyright annotation template](references/copyright-annotation-template.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Shared vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text recommendations with structured resource-entry field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing outputs include search results, reuse recommendations, tagging guidance, copyright-status guidance, and verification reminders for AI-generated questions.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
