## Description:

Auto-generate prerequisite maps for learning any topic, showing what to learn first, what depends on what, and a practical learning path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External learners, students, mentors, and career changers use this skill to map prerequisites, audit existing knowledge, and generate sequenced study plans for complex topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can read a user-specified custom graph JSON file.

Mitigation: Use custom graph files from trusted locations and review their concept structure before generating plans.

Risk: The CLI can write results to a user-specified output path.

Mitigation: Choose output paths intentionally to avoid overwriting unrelated files.

## Reference(s):

- [Custom Concept Graphs](references/custom-graphs.md)
- [Learning Theory](references/learning-theory.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/concept-cartographer)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/concept-cartographer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON learning path files, text trees, and Mermaid diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read a user-selected custom graph JSON file and write user-selected JSON, text, or Mermaid output files.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
