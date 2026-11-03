## Description:

Use only when explicitly invoked for software design, specifications, implementation, review, refactoring, or explanation with Daniel Jackson's concepts and synchronizations. Put functionality in independent modules and coordination in explicit rules to make software more modular, transparent, and easier to understand and change. Express the business in a shared language, organize concepts within clear boundaries, keep business rules independent and dependency direction explicit, and stay consistent from design to code. Check CONCEPT.md/SYNCS.md structure and generate Mermaid relationship maps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and software designers use this skill to model software behavior as independent concepts coordinated by explicit rules, create or maintain CONCEPT/SYNCS specifications, and review or implement changes while checking boundaries and assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram generation reads matching specification files throughout the selected project root, even when a narrower scope is supplied.

Mitigation: Choose the project root and output file deliberately; keep the root limited to the intended project area.

Risk: Bundled checks assess document structure and do not establish runtime correctness.

Mitigation: Review implementation behavior and relevant tests separately from specification-structure checks.

## Reference(s):

- [Specification format](references/spec-format.md)
- [Concept qualification criteria](references/criteria.md)
- [Engineering architecture guidance](references/engineering/architecture.md)
- [Jackson, Towards a Theory of Conceptual Design for Software](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [The Essence of Software: Concept Criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)
- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands]

**Output Format:** [Markdown specifications and review findings, Mermaid diagrams, and scoped code or documentation changes as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output varies by selected workflow; bundled checks assess document structure and do not establish runtime correctness.]

## Skill Version(s):

2.0.2 (source: artifact frontmatter; matches server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
