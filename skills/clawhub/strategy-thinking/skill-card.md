## Description:

A Chinese-language strategy-planning assistant that helps users clarify desired outcomes, diagnose core problems, evaluate conditions and resources, compare paths, and define executable next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhonnylau](https://clawhub.ai/user/jhonnylau)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have an action-oriented goal, problem, decision, or plan that needs structured strategy thinking rather than a fixed document template. It guides the conversation from desired result through problem diagnosis, path selection, risk awareness, and an executable next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning guidance can be misleading when important user facts or market assumptions are missing.

Mitigation: Keep unknowns explicit as UNKNOWN, [假设], or [需确认], and base recommendations only on user-provided facts, supplied materials, completed research, or arithmetic.

Risk: The opinionated planning structure may add unnecessary process to simple requests.

Mitigation: Use the skill's Quick, Standard, or Deep output depth according to task complexity and skip modules that do not affect the next decision.

Risk: The inspected artifacts are Chinese-oriented, which may not fit teams expecting English planning documentation.

Mitigation: Use this skill when Chinese strategy-planning guidance is appropriate, or explicitly request language adaptation during review.

## Reference(s):

- [strategy-thinking ClawHub skill page](https://clawhub.ai/jhonnylau/skills/strategy-thinking)
- [方法核心 V1.0 - 策划思维模型正式定义](references/method-core-v1.md)
- [Runtime 设计 V1.0 - 详细规格](references/runtime-design-v1.md)
- [C 层启发式 V1.0](references/heuristics-v1.md)
- [测试用例 V1.0 - 验收标准 + 攻击测试](references/test-cases-v1.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured planning sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language planning output; marks assumptions and items needing confirmation when evidence is missing.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter lists 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
