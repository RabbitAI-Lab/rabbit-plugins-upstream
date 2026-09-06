## Description:

初中物理概念的直觉建立器，用生活类比、头脑实验、公式推导三种模型把概念从“背下来”变成“真的懂了”。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to explain Chinese middle-school physics concepts through familiar analogies, mental experiments, and formula meaning checks. It is intended for concept intuition and validation, not step-by-step solving of a specific physics problem.

### Deployment Geography for Use:

China Mainland by default; localize curriculum assumptions, privacy rules, and crisis-contact guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Persistent learning-profile updates for minors may occur without independently enforced consent controls.

Mitigation: Require the hosting platform to keep profiles disabled by default, check age band, require guardian consent where applicable, and enforce cross-skill sharing consent before any profile writeback.

Risk: Default crisis-contact guidance and curriculum assumptions are designed for mainland China.

Mitigation: Localize emergency contacts, privacy requirements, and curriculum mappings before making the skill available outside mainland China.

Risk: Generated concept checks or practice prompts can contain inaccurate physics quantities or unsuitable difficulty.

Mitigation: Apply the bundled AI item self-check before presenting generated questions, including solvability, unit, quantity, and grade-band checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-concept-intuition)
- [物理概念生活类比素材库](artifact/references/physics-analogy-bank.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [全库统一词表](artifact/shared/vocab.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown with analogy prompts, concept checks, formula explanations, and optional structured handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request Learning DNA profile writeback or reminder enqueue only after the required consent checks; otherwise uses current-session context.]

## Skill Version(s):

2.1.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
