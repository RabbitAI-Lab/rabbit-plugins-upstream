## Description:

数学错误DNA helps agents analyze middle-school math mistakes by refining broad error categories into math-specific subtypes, identifying recurring root causes, and producing learner-facing weakness reports or next-step guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to turn repeated middle-school math mistakes into specific subtype diagnoses, weakness tracking, practice guidance, and on-request monthly math weakness reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store or share error-analysis data for minor students.

Mitigation: Install only where consent fields are enforced for profile storage, parent sharing, emotion sharing, and cross-skill sharing.

Risk: Generated math practice items or diagnoses may be incorrect or unsupported.

Mitigation: Require the built-in AI item self-check before learner use and mark teacher-facing generated items for human verification before resource-bank or exam use.

Risk: Historical statistics or weakness labels may be fabricated if cross-session memory or authoritative notebook counts are unavailable.

Mitigation: Use only current-session counts or label archive-derived statements as preliminary trends, and keep occurrence counts and status decisions with the correction-notebook authority.

Risk: Crisis or severe distress signals could be mishandled as ordinary math anxiety.

Mitigation: Run the crisis exception first, stop normal learning flows when crisis signals appear, avoid recording sensitive details, and localize emergency guidance by region.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [数学错因维度表](references/math-error-dimension-table.md)
- [初中数学高频概念混淆对照表](references/concept-confusion-map.md)
- [数学读题失误训练方法手册](references/reading-habits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown reports, short learner-facing text, and structured handover or reminder payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include math error subtype IDs, confidence labels, consent-gated profile updates, and reminder enqueue guidance.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
