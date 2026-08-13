## Description:

Auto-generate prerequisite maps for learning any topic — shows what to learn first, what depends on what, and the optimal learning path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Self-directed learners, students, mentors, and developers use this skill to map prerequisites, audit existing knowledge, and generate sequenced learning paths for complex topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Python helper can read a user-provided custom graph JSON path and write output to a user-provided path.

Mitigation: Use trusted graph files and choose output paths deliberately before running commands that include --graph or --output.

Risk: Generated prerequisite plans can be incomplete or misleading if the concept graph does not match the learner's goals or background.

Mitigation: Review the generated path and adjust known concepts or custom graph definitions before using the plan for study decisions.

## Reference(s):

- [Concept Cartographer GitHub repository](https://github.com/voronindenis5/concept-cartographer)
- [Concept Cartographer ClawHub page](https://clawhub.ai/voronindenis5/skills/concept-cartographer)
- [Custom Concept Graphs](references/custom-graphs.md)
- [Learning Theory: The Science of Prerequisite Sequencing](references/learning-theory.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus optional text, JSON, or Mermaid outputs from the bundled Python helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can print prerequisite maps, learning paths, audits, topic lists, and visualizations, and can optionally save JSON or Mermaid/text output to user-provided paths.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; source skill frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
