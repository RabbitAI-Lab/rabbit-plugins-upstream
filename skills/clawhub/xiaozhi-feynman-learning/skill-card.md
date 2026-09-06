## Description:

This Chinese K-12 learning skill guides a student through Feynman-style explanation, questioning, transfer, and critical-verification checks to assess whether a concept is memorized, explainable, or truly mastered.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, tutors, and education agents use this skill to test concept understanding after study, wrong-answer remediation, exam review, or AI-answer exposure. It produces a mastery judgment, identifies the point where the student got stuck, and only writes back minimal understanding data when explicit consent gates are satisfied.

### Deployment Geography for Use:

China mainland by default; localize crisis contacts and minor-data consent rules before non-mainland deployments.

## Known Risks and Mitigations:

Risk: The security evidence flags the release as suspicious because the persistent student-profile writeback schema is broader than the skill's stated scope.

Mitigation: Before deployment, enforce sender-to-path authorization outside the package schema and reject profile patches outside extensions.understanding.

Risk: The skill can request profile writeback and reminder handoff for minor learners.

Mitigation: Require explicit user consent for profile writeback and reminder enqueueing, and apply local guardian-consent rules before enabling long-term records.

Risk: Crisis-support contact details are designed for China mainland and may be inappropriate elsewhere.

Mitigation: For non-mainland deployments, localize emergency contacts, youth-support channels, and minor-data consent rules before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Feynman 4+1 jump state machine](references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Multi-agent handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Platform conventions and deployment localization](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational guidance and markdown-style assessment summaries, with optional JSON handoff payloads for profile writeback or reminder enqueueing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default operation is session-local; profile writeback and reminder handoff require explicit consent.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
