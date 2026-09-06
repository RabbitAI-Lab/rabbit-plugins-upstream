## Description:

复习规划师 helps teachers turn broad review requests into knowledge maps, prioritized review scope, spaced-recall schedules, interleaved practice groups, review activities, and exam-eve state guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to plan unit, midterm, final, or pre-exam review around classroom weaknesses, knowledge maps, spacing, interleaving, and classroom-safe exam preparation. It produces review plans rather than full assignments, exams, or lesson plans.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of crisis resources, curriculum assumptions, and minor-data consent requirements.

## Known Risks and Mitigations:

Risk: Review plans could be saved with incorrect scope or stale classroom assumptions.

Mitigation: Show the full schedule to the teacher and require explicit confirmation before writing to classWorkspace.reviewPlans.

Risk: Classroom review artifacts could expose student identities or sensitive achievement data.

Mitigation: Write only knowledge-point level aggregate signals, use pseudonyms or seat numbers when a student reference is necessary, and exclude individual scores, rankings, and score-band positions.

Risk: Crisis or severe distress signals could be mistaken for ordinary exam stress.

Mitigation: Stop review planning when crisis signals appear, use the bundled crisis referral protocol, and localize emergency resources before deployment outside mainland China.

Risk: AI-generated example or variant questions may contain mistakes.

Mitigation: Run the bundled AI item self-check, label teacher-facing generated items for human verification, and route full assignment or exam generation to the dedicated downstream skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Review strategy](references/review-strategy.md)
- [Knowledge map example](references/knowledge-map-example.md)
- [Key points checklist template](references/key-points-checklist-template.md)
- [Review activity library](references/review-activity-library.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [AI item check protocol](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown tables and structured classWorkspace.reviewPlans fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before persistent writeback; student identifiers are pseudonymized and individual scores or rankings are excluded.]

## Skill Version(s):

2.1.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
