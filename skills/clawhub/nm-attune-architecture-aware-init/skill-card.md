## Description:

Selects architecture paradigm via research before scaffolding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when starting a project whose architecture is undecided and the decision needs research, justification, scaffolding, and an ADR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scaffolds and ADRs may encode an architecture choice that does not fit the project context.

Mitigation: Review the research brief, selected paradigm, scaffold diff, and ADR before keeping or committing the generated output.

Risk: Optional Night Market automation commands may run external plugin scripts outside the skill artifact.

Mitigation: Inspect those scripts separately and run the automation deliberately only after confirming the commands and output paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-architecture-aware-init)
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [Architecture Research Flow](artifact/modules/research-flow.md)
- [Paradigm Selection](artifact/modules/paradigm-selection.md)
- [Scaffold Generation](artifact/modules/scaffold-generation.md)
- [Script Integration](artifact/modules/script-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code blocks, and generated project file content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include online research synthesis, architecture decision rationale, directory structures, configuration hints, and ADR content.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
