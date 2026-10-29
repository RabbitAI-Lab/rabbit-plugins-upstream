## Description:

Compare Rotifer Genes in the Arena and produce Markdown reports with fitness and security grades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to compare Rotifer Genes or evaluate another Skill after choosing to import it as a Gene. It produces an Arena report with fitness rankings and security grades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party Rotifer CLI and its npm cache may write outside the project.

Mitigation: Review the package and installation effects before approving installation; use an existing trusted installation when available.

Risk: Arena evaluation uses network access and selected Genes, and saving a report or publishing changes project or cloud state.

Mitigation: Review the selected Genes and proposed opponent; require explicit approval before publishing or saving a report.

## Reference(s):

- [Rotifer Protocol Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Playground repository (linked in the artifact manifest)](https://github.com/rotifer-protocol/rotifer-playground)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [ClawHub release page](https://clawhub.ai/xiaoba-dev/skills/rotifer-arena)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown Arena report with comparison tables, rankings, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report saving and Cloud publishing require explicit user choice.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
