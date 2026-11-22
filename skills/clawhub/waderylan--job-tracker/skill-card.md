## Description:

Track job applications from recruiting emails the user shares or another skill provides. Labels each email, applies a fixed status transition table, records deadlines and interviews, and reports the funnel, response rate, time in stage, follow-ups due and ghosted applications. Stores everything in one workspace file; no credentials or network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[waderylan](https://clawhub.ai/user/waderylan)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers use this skill to organize applications from recruiting emails, track interview and deadline details, and review their application progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a low-severity inconsistency around views that may make confirmed status changes, and notes that scan coverage is incomplete because a referenced runtime file was missing.

Mitigation: Review tracker state after confirming a status change and check the referenced runtime file before relying on report behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/waderylan/skills/job-tracker)
- [Publisher profile](https://clawhub.ai/user/waderylan)
- [Labels and stages](references/labels.md)
- [Status transition rules](references/transitions.md)
- [Deadlines and interview times](references/deadlines.md)
- [Application record schema](references/record-schema.md)
- [Computed reports](references/views.md)
- [Interview preparation](references/interview-prep.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON workspace records, concise text reports, and interview-preparation search queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records are kept in one workspace file; interview-preparation queries are suggestions and are not run by the skill.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
