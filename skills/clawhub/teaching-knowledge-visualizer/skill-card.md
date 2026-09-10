## Description:

Teaching Knowledge Visualizer helps teachers turn lesson topics, chapter material, and textbook text into classroom-ready visual teaching materials, including interactive HTML pages for concept maps, diagrams, timelines, comparison tables, function plots, and quizzes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maguangcaii](https://clawhub.ai/user/maguangcaii)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education-focused agents use this skill to structure subject matter, select an appropriate visual form, prepare a JSON outline for teacher confirmation, and generate self-contained classroom HTML materials. It is aimed at lesson preparation, classroom projection, unit review, board-design alternatives, and student self-study.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Interactive function pages may evaluate configurable math expressions in browser JavaScript.

Mitigation: Review generated HTML before classroom use and avoid untrusted pasted or web-retrieved expression content until the evaluator is replaced with a real math parser or strict AST interpreter.

Risk: Artifact documentation may contain internal provenance metadata.

Mitigation: Ask the publisher to scrub internal provenance metadata from pedagogy.md before public redistribution.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Data format specification](artifact/data-format.md)
- [Pedagogy notes](artifact/pedagogy.md)
- [ClawHub skill page](https://clawhub.ai/maguangcaii/skills/teaching-knowledge-visualizer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration and self-contained HTML/CSS/JavaScript output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce one or two HTML files; Mermaid, PlantUML, or Markdown graph source is produced only when explicitly requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
