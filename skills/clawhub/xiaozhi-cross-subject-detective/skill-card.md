## Description:

用一个真实主题在一周内串联多门学科，找出学科之间的联结。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students in upper elementary, middle school, and high school use this skill to investigate a real-world topic across subjects, identify connections, and turn the work into project records and concept-map entries. It also supports educator- or guardian-guided interdisciplinary inquiry when age and consent requirements apply.

### Deployment Geography for Use:

Global; localize crisis and emergency-resource text before use outside Mainland China.

## Known Risks and Mitigations:

Risk: The skill can maintain cross-subject project records and share limited study summaries with related Xiaozhi skills.

Mitigation: Confirm user intent and honor the documented view, correct, delete, pause, export, and sharing-control commands before maintaining or sharing records.

Risk: Crisis hotline and emergency-resource text is locale-specific.

Mitigation: Replace Mainland-China-specific emergency and crisis resources with local resources before use in other regions.

Risk: Generated practice items or cross-subject explanations could be inaccurate or outside the learner's grade band.

Mitigation: Apply the bundled AI item self-check protocol, grade-band limits, and human review for teacher-facing resource use.

Risk: The skill depends on memory-style platform capability for week-long project continuity.

Mitigation: When cross-session memory is unavailable, limit the interaction to the current session and provide daily records the student can save.

## Reference(s):

- [Project Record Template](artifact/references/detective-project-template.md)
- [Cross-Subject Connection Templates](artifact/shared/cross-subject-connections.md)
- [Hint Ladder](artifact/shared/hint-ladder.md)
- [Grade Bands](artifact/shared/grade-bands.md)
- [AI Item Self-Check Protocol](artifact/shared/ai-item-check.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown-style educational guidance with structured project records and concept-connection entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce student-confirmed project records, concept graph nodes and edges, hints, summaries, and exportable text records.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
