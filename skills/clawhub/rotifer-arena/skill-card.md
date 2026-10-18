## Description:

Compares Rotifer Genes in the Arena and reports fitness, security grades, rankings, and improvement options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to compare Rotifer Genes, evaluate Arena fitness and security grades, and generate a reproducible Markdown comparison report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may fetch and run the Rotifer CLI from npm.

Mitigation: Review the package and pin its version before installing or running it.

Risk: CLI operations read and write project Gene artifacts and contact the Rotifer API.

Mitigation: Review commands before running them and avoid sensitive projects unless those file and network operations are acceptable.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Arena on ClawHub](https://clawhub.ai/xiaoba-dev/skills/rotifer-arena)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown comparison report with tables and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes F(g) fitness, V(g) security grades, rankings, and upgrade guidance when available.]

## Skill Version(s):

1.2.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
