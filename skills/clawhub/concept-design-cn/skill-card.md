## Description:

仅在显式调用时使用。用 Daniel Jackson 的概念与同步方法设计、实现、审查和重构软件，编写规格并解释软件行为。检查 CONCEPT.md/SYNCS.md 结构，生成 Mermaid 关系图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

开发者可用此技能按用户所需行为设计软件概念与同步规则，编写和检查规格，辅助实现、重构、审查及解释软件行为。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 关系图生成会读取选定项目根目录中的规格；--scope 仅限制展示内容，可能导致对实际读取范围的误解。

Mitigation: 将根目录设为明确的项目目录，并确认其中的规格文件符合预期。

Risk: 实现模式会修改范围内文件，而运行时权限强制尚未验证。

Mitigation: 接受实现变更前审查差异；使用只读工作流时检查是否产生文件变更，并在受控副本中确认权限边界。

## Reference(s):

- [ClawHub 发布页](https://clawhub.ai/agenticweb4/skills/concept-design-cn)
- [CONCEPT/SYNCS 格式](artifact/references/spec-format.md)
- [Meng 与 Jackson，WYSIWID v2](https://arxiv.org/html/2508.14511v2#S4)
- [Jackson，Beyond Objects v1](https://arxiv.org/html/2606.27258v1#S12)
- [Jackson，Concept criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Jackson，Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Mermaid diagrams]

**Output Format:** [Markdown with CONCEPT/SYNCS specifications, Mermaid diagrams, code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explicit invocation only; review, audit, and drift workflows are read-only, while other work is limited to the requested scope.]

## Skill Version(s):

2.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
