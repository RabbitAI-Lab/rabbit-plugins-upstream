## Description:

仅在显式调用时使用。用 Daniel Jackson 的概念与同步方法设计、实现、审查和重构软件，编写规格并解释软件行为。检查 CONCEPT.md/SYNCS.md 结构，生成 Mermaid 关系图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design software around independent concepts and synchronization rules, write and review specifications, implement or refactor within an authorized scope, and explain behavior with evidence. It can also check CONCEPT.md and SYNCS.md structure and generate Mermaid relationship diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is benign with medium confidence, but two unresolved local references leave evidence incomplete.

Mitigation: Review the unresolved references and the skill's file, network, and shell capabilities before installation; confirm how the host runtime enforces permissions.

## Reference(s):

- [Concept composition and sync — Daniel Jackson](https://essenceofsoftware.com/tutorials/concept-basics/sync/#composing-concepts-with-syncs)
- [Domain-Driven Design reference](https://www.domainlanguage.com/ddd/reference/)
- [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Hexagonal Architecture — Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture)
- [ClawHub release page](https://clawhub.ai/agenticweb4/skills/concept-design-cn)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown, including software specifications, review findings, Mermaid diagrams, and code or shell commands when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language follows the user's request; diagram and checker results should state unsupported or unverified areas.]

## Skill Version(s):

2.4.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
