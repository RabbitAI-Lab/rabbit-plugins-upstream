## Description:

微观世界想象器帮助中文 K12 学生用分子、原子、离子等粒子图景解释化学现象、化学变化、质量守恒、溶解、电离和电子转移。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, teachers, and education platforms use this skill to explain chemistry concepts in Chinese through particle-level reasoning, text particle diagrams, bounded analogies, and misconception checks. It is intended for Mainland China K12 chemistry contexts unless curriculum assumptions, consent rules, and crisis-support contacts are localized.

### Deployment Geography for Use:

China (Mainland China curriculum context)

## Known Risks and Mitigations:

Risk: The skill is designed for Mainland China K12 chemistry, consent, and crisis-support assumptions.

Mitigation: Use it in that context by default; before deployment elsewhere, localize curriculum scope, consent rules, and emergency or youth-support contacts.

Risk: Minor learners' profile data can be sensitive if platform controls do not enforce consent boundaries.

Mitigation: Require consent-gated profile access, limit reads to relevant chemistry subtype signals, honor view/correct/delete/pause/export controls, and keep this skill from writing profile records.

Risk: Chemistry experiment questions can lead to unsafe home experimentation.

Mitigation: Do not provide dangerous home experiment steps; explain principles, defer hands-on work to teacher-supervised school labs, and follow the bundled lab-safety rules.

Risk: Students may ask for help during an active exam or test.

Mitigation: Do not provide hints or answers for active exams; ask whether the assessment is over when unclear and offer post-exam review instead.

Risk: Analogies can create or reinforce chemistry misconceptions when their limits are omitted.

Mitigation: Pair every analogy with an explicit failure boundary and a check question that asks the learner to restate the concept in particle language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-micro-visualizer)
- [化学粒子类比库](references/chemistry-micro-analogy-bank.md)
- [DNA profile schema](shared/dna-profile.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [实验安全约定](shared/lab-safety.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [AI 出题自检协议](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown/plain text explanations with text particle diagrams, analogies, misconception checks, and practice prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads consent-gated chemistry profile signals when enabled, does not write the profile, and follows safety, exam-integrity, and crisis-referral boundaries.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
