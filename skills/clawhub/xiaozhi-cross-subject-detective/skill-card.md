## Description:

跨学科侦探周 guides Chinese K12 learners through a week-long, student-led project that connects a real theme across subjects, records project progress, and writes confirmed concept connections back to a learning profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle school, and high school use this skill with a learning agent to choose a real topic, explore it from multiple subject perspectives, identify connections, and produce a project record for confirmed profile writeback. Educators or guardians may use the outputs to review cross-subject learning progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term learning profile records may contain student learning history, project interests, and concept connections.

Mitigation: Enable long-term profiles only with required student or guardian consent, and honor view, correction, deletion, export, pause, and sharing-control requests.

Risk: Project records may be shared across skills or with parents beyond the student's intended audience.

Mitigation: Use the skill's sharing controls and confirmation flow before profile writeback, cross-skill sharing, or parent-visible summaries.

Risk: Generated study prompts or temporary quiz items may be incorrect or unsuitable for the learner's grade band.

Mitigation: Apply the bundled AI item self-check and require teacher review before generated items are stored in a resource bank or test.

Risk: Crisis-support language includes mainland China-specific contact numbers.

Mitigation: Localize emergency and youth support channels before deployment outside mainland China; when location is unknown, ask for the learner's country or region before giving phone numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cross-subject-detective)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Detective project template](artifact/references/detective-project-template.md)
- [Cross-subject connection templates](artifact/shared/cross-subject-connections.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Grade bands](artifact/shared/grade-bands.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Public handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational guidance plus structured Markdown/text project records and JSON-compatible profile writeback payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile and concept-graph updates require confirmation; the skill does not produce shell commands or executable code.]

## Skill Version(s):

2.1.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
