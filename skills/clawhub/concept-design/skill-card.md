## Description:

Guides agents in designing, specifying, implementing, reviewing, and explaining modular software with independent concepts and explicit synchronization rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to model software around independent concepts and explicit synchronization rules, then create or maintain specifications, diagrams, and implementations that are easier to understand and change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selecting the wrong project root can make relationship maps incomplete or misleading, because specification indexing covers that root.

Mitigation: Confirm the project root before mapping; use --scope only to limit displayed relationships.

Risk: Design proposals or generated changes may encode incorrect assumptions.

Mitigation: Review changes against requirements and evidence; use stdout or --check for read-only work.

## Reference(s):

- [Jackson, Towards a Theory of Conceptual Design for Software](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [The Essence of Software: qualification](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Meng & Jackson, WYSIWID v1](https://arxiv.org/abs/2508.14511v1)
- [Beyond Objects v1, §§12–13](https://arxiv.org/html/2606.27258v1#S12)
- [Jackson, Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)
- [ub-mode skill](https://github.com/unclebob/ub-mode/blob/master/SKILL.md)
- [Concept Design on ClawHub](https://clawhub.ai/agenticweb4/skills/concept-design)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown specifications and Mermaid diagrams, with code or review findings when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope depends on the requested workflow; review, audit, drift, and plan-only work is read-only.]

## Skill Version(s):

2.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
