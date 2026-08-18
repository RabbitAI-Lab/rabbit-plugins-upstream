## Description:

One-click Gene comparison and evaluation that imports Rotifer Genes from ClawHub, local files, or scratch, compiles them, matches opponents, runs Arena battles, and generates Markdown reports with fitness scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to compare Rotifer Genes, import skills as Genes when needed, run Rotifer Arena evaluations, and generate decision-focused Markdown reports with fitness and security grades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rotifer CLI workflows can read project Gene files, write project artifacts, and contact the public Rotifer API.

Mitigation: Install only for intended Rotifer CLI use and review proposed commands before approving installs, publishing, overwrites, or report saves.

Risk: Evaluation reports can mislead readers if metrics are guessed or mixed across Arena fitness, security grades, and adoption data.

Mitigation: Use only values from commands that were actually run, keep Arena F(g), V(g), and adoption comparisons separate, and leave unsupported metrics blank with a short explanation.

## Reference(s):

- [Rotifer Arena on ClawHub](https://clawhub.ai/xiaoba-dev/skills/rotifer-arena)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with command blocks and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write reports under arena-reports/ only after the user asks to save.]

## Skill Version(s):

1.2.1 (source: server release evidence and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
