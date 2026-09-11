## Description:

Coordinates Xiaozhi learning-system skills by routing study requests, avoiding duplicate handoffs, and generating consent-based monthly learning summaries when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, teachers, and learning-support agents use this skill to decide which Xiaozhi learning skill should handle a study request and to assemble authorized summaries across error review, understanding checks, notes, planning, focus, and reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The student-data handover schema is broader than the coordinator role and may expose more records than a routing task requires.

Mitigation: Install only where route authorization, exact payload filtering, and minimum-necessary field selection are enforced outside the schema.

Risk: Student records, teacher writebacks, and reminder queues may be used without the learner's current sharing expectations.

Mitigation: Require fresh consent checks and user controls for cross-skill sharing, teacher writeback, reminders, parent-visible output, correction, deletion, export, and pause requests.

Risk: A learning workflow could continue after self-harm, bullying, family-safety, or severe despair signals.

Mitigation: Stop routing, reporting, data display, and parent-summary flows and follow the bundled crisis referral protocol before any learning-system action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Complete one-week linkage record](references/one-week-linkage-record.md)
- [Handover protocol schema](schemas/handover-protocol.schema.json)
- [Shared vocabulary and consent fields](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions and degradation paths](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Configuration]

**Output Format:** [Natural-language routing guidance, Markdown learning summaries, and schema-constrained JSON handover payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses minimum necessary fields and consent-gated handoffs; does not independently teach, analyze root causes, create exercises, or send reminders.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
