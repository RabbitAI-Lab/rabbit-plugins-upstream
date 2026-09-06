## Description:

初中物理实验思维教练，帮助学生用苏格拉底式提问理解物理实验方法、变量控制、数据处理、误差分析和实验评价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and education agents use this skill to coach Chinese middle-school physics experiment thinking, including experiment design, variable control, data-table or graph analysis, conclusions, and error review. It is intended for tutoring support rather than replacing teacher review of generated exercises or safety-sensitive student support.

### Deployment Geography for Use:

Global, with localization required for users outside mainland China

## Known Risks and Mitigations:

Risk: The skill may use student learning profiles, cross-skill handoffs, OCR of submitted experiment images, and consent-based reminder queueing.

Mitigation: Confirm user and guardian consent where required, honor the documented profile controls, and use the no-memory, no-OCR, or no-reminder fallbacks when those platform capabilities or permissions are unavailable.

Risk: Safety-referral and minor-data assumptions are written for mainland China and may be inappropriate in other regions.

Mitigation: Localize emergency contacts, school-stage assumptions, and minor-data consent requirements before deploying to users outside mainland China.

Risk: Generated practice items or experiment explanations can be incorrect or over-complete for a learning context.

Mitigation: Apply the bundled AI item self-check, keep Socratic scaffolding as the default, and require teacher or operator review before generated items enter a resource bank or assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-lab-coach)
- [物理实验方法深度手册](references/physics-experiment-methods.md)
- [物理数据分析方法手册](references/physics-data-analysis.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tutoring guidance with questions, tables, and optional structured handoff entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language middle-school physics support; may rely on platform OCR, memory, and reminder capabilities with documented fallbacks.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
