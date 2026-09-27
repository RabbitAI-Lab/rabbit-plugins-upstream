## Description:

Helps independent teachers organize, search, adapt, and track reusable teaching materials and anonymized learning cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to maintain a searchable library of handouts, exercises, teaching explanations, lesson plans, and anonymized error cases, then adapt suitable materials for future lessons.

### Deployment Geography for Use:

Mainland China (simplified-Chinese K–12 teaching context)

## Known Risks and Mitigations:

Risk: Persistent resource entries or case notes could expose identifiable student information.

Mitigation: Confirm consent, de-identify cases before storage, and exclude real names, schools, contact details, and identifying details.

Risk: Stored question text or scans could reproduce material without authorization.

Mitigation: Record copyright status and source; store only bibliographic indexes for textbook exercises and past exam questions, not their text or scans.

Risk: Unverified AI-generated exercises could contain errors if reused with students.

Mitigation: Label AI-generated items and exclude them from student recommendations until a teacher checks each question.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization and retrieval](references/resource-categorization.md)
- [Resource entry examples](references/resource-entry-examples.md)
- [Copyright annotation template](references/copyright-annotation-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language search results, adaptation guidance, and structured resource-library entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing; resource entries may persist for later retrieval and reuse.]

## Skill Version(s):

2.7.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
