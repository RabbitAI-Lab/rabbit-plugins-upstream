## Description:

用《AI超级个体》第二章的 KANO 框架把需求分为基本型、期望型、魅力型、无差异型或反向型，并按“先补底线、再做增益、最后上惊喜”生成可解释的产品优先级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cglt2026opc](https://clawhub.ai/user/cglt2026opc)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, founders, and product teams use this skill to classify candidate requirements with a simplified KANO method and turn the classifications into an explainable priority order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weak or incomplete requirement evidence can produce provisional KANO classifications that look more certain than they are.

Mitigation: Label low-evidence classifications as tentative and validate disputed items with user interviews, usability testing, or business constraints before acting.

Risk: The optional sorter reads a local JSON file selected by the user.

Mitigation: Run the sorter only on trusted JSON files containing product requirements and evidence intended for this analysis.

## Reference(s):

- [KANO 分类与排序](references/kano.md)
- [ClawHub skill page](https://clawhub.ai/cglt2026opc/skills/kano-prioritizer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional JSON input and JSON-sorted output from the local script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The sorter expects a JSON list of requirement items with KANO type, impact, evidence, and effort fields.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
