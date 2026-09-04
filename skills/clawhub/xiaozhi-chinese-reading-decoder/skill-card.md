## Description:

阅读理解拆解师 coaches students through modern Chinese reading-comprehension practice by separating passage understanding from exam-style answer structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners use this skill to practice modern Chinese reading-comprehension tasks, including prose, argumentative, explanatory, and non-continuous texts. It helps students diagnose common answer-pattern issues, locate textual evidence, and revise answers after making their own attempt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use long-term learning-profile storage and cross-skill sharing for reading-pattern support.

Mitigation: Keep profile and cross-skill sharing disabled unless needed, and use the provided view, correct, delete, pause, sharing, and export controls.

Risk: The bundled crisis and emergency resources are China-specific.

Mitigation: Localize crisis or emergency resources before use with learners outside Mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [语文错因维度表](artifact/references/chinese-error-dimension-table.md)
- [阅读五坑专项训练策略](artifact/references/pit-training.md)
- [现代文各题型出题逻辑与答题模板详解](artifact/references/question-type-library.md)
- [学习DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown conversational guidance with optional structured profile handoff data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps coaching responses concise and uses consent-gated profile controls when memory or cross-skill sharing is available.]

## Skill Version(s):

2.1.0 (source: evidence release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
