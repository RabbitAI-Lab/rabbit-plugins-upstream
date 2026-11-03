## Description:

以概念与同步方法帮助开发者设计、规格化、实现、审查和解释软件架构，并支持检查 CONCEPT.md/SYNCS.md 与生成 Mermaid 关系图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和软件架构师可用此技能梳理业务概念与协作规则，编写规格，实施或审查范围内的代码变更，并生成或检查概念关系图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 图表生成会递归读取目标目录下的 CONCEPT.md 和 SYNCS.md，目录选错时可能纳入无关规格。

Mitigation: 运行图表生成前确认项目根目录和扫描范围。

Risk: 实现和精炼模式可能修改项目文件。

Mitigation: 限定任务范围，并在保留或应用变更前审阅差异。

Risk: 生成的图表和语法检查不能证明软件行为正确。

Mitigation: 结合源码审查及适用的测试验证契约、运作原理和应用场景。

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/concept-design-cn)
- [Jackson, Towards a Theory of Conceptual Design for Software](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [The Essence of Software: Concept Criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Jackson, Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands]

**Output Format:** [中文 Markdown，包含概念规格、Mermaid 图、代码修改建议或检查结果]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按请求限定设计、规格、实现、审查、维护或解释范围。]

## Skill Version(s):

2.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
