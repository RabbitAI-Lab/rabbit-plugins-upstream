## Description:

A Simplified Chinese middle-school physics tutoring skill that analyzes wrong-answer patterns across physics visualization, concepts, formulas, process reasoning, and math-tool use, then produces weakness reports and consent-gated archive updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External education agents and learners use this skill to identify recurring root causes in middle-school physics mistakes, produce concise weakness reports, and coordinate consent-gated writebacks with adjacent learning-record and reminder skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process records for minors and generate parent-visible summaries.

Mitigation: Verify profile, guardian, parent-sharing, and emotion-sharing consent before reading, writing, or sharing learner records; keep outputs to the student when consent is absent.

Risk: Physics anxiety content can include crisis signals that exceed learning support.

Mitigation: Apply the bundled crisis-exception protocol before tutoring or reporting, record only the referral fact, and localize emergency resources for the learner's region.

Risk: Weakness reports can become misleading if generated from too little data or from unavailable history.

Mitigation: Use the skill's confidence labels, mark insufficient samples clearly, and avoid monthly or cross-session statistics when the required history is unavailable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [Physics error dimension table](artifact/references/physics-error-dimension-table.md)
- [Physics concept confusion map](artifact/references/physics-concept-confusion-map.md)
- [Physics math tools checklist](artifact/references/physics-math-tools-checklist.md)
- [Physics diagram guide](artifact/shared/physics-diagram-guide.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text for learner-facing analysis, with structured JSON-shaped handover records when consent permits updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve sample-size confidence labels, avoid unsupported historical counts, and respect profile, sharing, parent-summary, emotion-sharing, and reminder consent gates.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
