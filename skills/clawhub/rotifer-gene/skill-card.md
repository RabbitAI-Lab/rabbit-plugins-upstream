## Description:

The Gene manual for Rotifer Protocol helps developers write a Gene's express function and phenotype schema, run the four-layer security audit before publishing, and migrate a Gene's fidelity from Wrapped to Hybrid or Native.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when building, auditing, publishing, benchmarking, or upgrading Rotifer Genes. It provides procedural guidance, example commands, schema patterns, and security audit checklists specific to Rotifer Gene projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rotifer CLI commands can execute processes, read and write project files, and fetch npx packages.

Mitigation: Review commands before running them and keep execution scoped to the intended project directory.

Risk: Publishing, login, cloud audit, and Arena submission commands can use network access and environment credentials.

Mitigation: Run the included audit checks before publishing, verify cloud commands and credential-bearing curl calls, and avoid publishing until findings are resolved.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground Repository](https://github.com/rotifer-protocol/rotifer-playground)
- [Rotifer Gene Skill Page](https://clawhub.ai/xiaoba-dev/skills/rotifer-gene)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, TypeScript examples, JSON configuration examples, and audit checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill does not perform actions on its own; it proposes Rotifer CLI workflows that the user reviews and runs.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
