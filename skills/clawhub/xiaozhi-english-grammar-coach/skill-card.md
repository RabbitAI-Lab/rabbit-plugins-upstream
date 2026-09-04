## Description:

A Chinese-language English grammar coach that uses guided questions to help middle-school students identify grammar errors and, with consent, record grammar weak points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to practice English grammar through short Socratic prompts, focused correction, and targeted grammar drills. When consent is enabled, it can maintain a grammar weakness profile and progress notes; otherwise it stays within the current session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term grammar profile records could be stored or shared without clear consent.

Mitigation: Enable profile writeback and cross-skill sharing only when the consent fields allow it; otherwise keep analysis within the current session and honor view, correct, delete, pause, share-control, and export requests.

Risk: Crisis referral guidance is written for mainland China and may be wrong or incomplete elsewhere.

Mitigation: Localize emergency and crisis-support channels before relying on the skill outside mainland China.

Risk: Agent-generated practice items could contain incorrect grammar, ambiguous answers, or content outside the declared grade band.

Mitigation: Apply the bundled AI item self-check before presenting generated exercises and require human review before adding generated items to teacher resources or assessments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [英语错因维度表](artifact/references/english-error-dimension-table.md)
- [五类语法错误详细分析与追问话术扩展库](artifact/references/grammar-patterns.md)
- [提示阶梯与完整示例出口](artifact/shared/hint-ladder.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language coaching responses, short Markdown summaries, guided practice prompts, and consent-gated profile update records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses session-only analysis when memory or cross-session statistics are unavailable; long-term profile updates require explicit consent.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
