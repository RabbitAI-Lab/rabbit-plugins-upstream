## Description:

仅在显式调用时，用 Daniel Jackson 的概念与同步方法设计、写规格、实现、审查、重构或解释软件。将功能放进独立模块，将协作写成明确规则，让软件更模块化、行为更透明、更容易理解与修改。支持 CONCEPT.md/SYNCS.md 结构检查与 Mermaid 关系图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design and document software around independent concepts and explicit coordination rules, then review specifications or code and make authorized changes. It can also check CONCEPT.md and SYNCS.md structure and generate a Mermaid architecture map.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagram generator reads matching specifications beneath the selected project root, including files outside a displayed --scope.

Mitigation: Choose the intended project root and review which specifications feed the generated map; use --check when comparing output without writing.

Risk: The structural linter does not establish semantic correctness, runtime behavior, or software security.

Mitigation: Pair structural checks with contract and code review, relevant tests, and security checks for the project.

## Reference(s):

- [Specification format](artifact/references/spec-format.md)
- [Design workflow](artifact/references/design.md)
- [Review workflow](artifact/references/review.md)
- [Concept and synchronization maps](artifact/references/guard/map.md)
- [Source references and local conventions](artifact/references/sources.md)
- [Towards a Theory of Conceptual Design for Software](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [The Essence of Software: Concept Criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)
- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown specifications, decision records, review findings, Mermaid diagrams, and code changes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope-specific; review, audit, drift, and planning work is read-only, while other changes stay within the authorized scope.]

## Skill Version(s):

2.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
