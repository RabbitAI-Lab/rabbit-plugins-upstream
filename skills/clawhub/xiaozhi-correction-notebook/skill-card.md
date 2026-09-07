## Description:

智能错题本 helps students record concrete wrong-answer cases, classify root causes across subjects, count recurring weak points, and prepare follow-up practice, reports, or handovers to subject-specific skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning assistants use this skill to turn specific wrong-answer cases into a correction notebook with root-cause labels, 28-day weak-point counts, similar-question practice, and semester-level summaries. It can also prepare consent-gated handover records for subject-specific analysis skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student learning records may be persisted or shared without sufficiently explicit confirmation.

Mitigation: Require explicit confirmation before each persistent write or cross-skill handover, treat silence as no consent, and verify guardian or profile consent when applicable.

Risk: Overly permissive handover validation may allow undocumented student data fields to be shared.

Mitigation: Restrict handover payloads to documented schema fields and share only the minimum data needed for subject-specific analysis.

Risk: Wrong-answer workflows may encounter minors' anxiety, self-harm, bullying, or safety signals.

Mitigation: Stop the learning workflow for crisis signals, follow the bundled crisis referral protocol, and record only the referral disposition.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error Analysis Framework](references/error-analysis-framework.md)
- [Handover Protocol Schema](shared/handover-protocol.schema.json)
- [Wrong Answer Handover Example](shared/wrong-answer-handover.example.json)
- [Deep Analysis Writeback Example](shared/deep-analysis-writeback.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration]

**Output Format:** [Conversational text, Markdown summaries and reports, and JSON handover or writeback records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent writes and cross-skill sharing should require explicit confirmation and documented consent.]

## Skill Version(s):

2.1.12 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
