## Description:

通过逐级提示和追问，帮助初高中学生分析数学题、订正错误、练习同类题并进行考前梳理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向初高中学生的数学单题辅导：引导学生定位卡点、订正解题步骤、练习同类题，并按需梳理考前知识点。默认仅在当前会话内使用；读取或共享学习记录须经当轮同意。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A student's learning record could be retained or shared without appropriate student or guardian consent.

Mitigation: Keep tutoring session-only by default; confirm current-session consent and age-appropriate guardian settings before enabling records or cross-skill sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Hint ladder](shared/hint-ladder.md)
- [Four-step tutoring workflow](references/photo-4step-statemachine.md)
- [Socratic questioning guide](references/math-socrates-guide.md)
- [High-school worked examples (introductory)](references/math-hs1-worked-examples.md)
- [High-school worked examples (core)](references/math-hs2-worked-examples.md)
- [High-school worked examples (advanced)](references/math-hs3-worked-examples.md)
- [Generated exercise quality checks](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Chinese-language chat text or Markdown; optional structured JSON handoff with consent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes graduated hints, worked explanations or practice problems; record handoff requires explicit consent.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
