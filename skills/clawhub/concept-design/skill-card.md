## Description:

Use only when explicitly invoked. Design, specify, implement, review, refactor, or explain software with Daniel Jackson's concepts and synchronizations. Check CONCEPT.md/SYNCS.md structure and generate Mermaid relationship diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design and explain software behavior, write concept and synchronization specifications, review designs, and guide scoped implementation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram mode reads matching specifications throughout the selected project root, even when --scope is supplied.

Mitigation: Choose a narrow project root and review the files that will be included before generating a diagram.

Risk: Implementation and diagram workflows can edit project files.

Mitigation: Review edits produced by these workflows; use review or audit workflows when read-only work is needed.

## Reference(s):

- [Meng & Jackson, WYSIWID v2](https://arxiv.org/html/2508.14511v2#S4)
- [Jackson, Beyond Objects v1, sections 12 and 13](https://arxiv.org/html/2606.27258v1#S12)
- [Jackson, Concept criteria](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Jackson, Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)
- [CONCEPT/SYNCS format](references/spec-format.md)
- [Concept and Synchronization Diagram format](references/map-format.md)
- [ClawHub release page](https://clawhub.ai/agenticweb4/skills/concept-design)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown specifications and reviews, Mermaid diagrams, code changes, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by selected workflow.]

## Skill Version(s):

2.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
