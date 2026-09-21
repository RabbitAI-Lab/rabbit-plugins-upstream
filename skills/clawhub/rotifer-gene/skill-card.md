## Description:

Rotifer Gene guides agents through building, auditing, publishing, and migrating Rotifer Genes with phenotype schemas, fidelity rules, security checks, and pinned Rotifer CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when creating Rotifer Genes, writing express functions and phenotype schemas, running security audits, publishing through the Rotifer CLI, or migrating fidelity from Wrapped to Hybrid or Native.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an assistant to propose Rotifer CLI commands that write generated Genes and compiled artifacts into the current project.

Mitigation: Review proposed commands and generated Gene files before execution, especially changes under genes/ and generated IR artifacts.

Risk: Publishing and Arena cloud submission can send Gene metadata, README content, phenotype data, and compiled artifacts to Rotifer services.

Mitigation: Run the documented four-layer audit before publishing, keep real credentials out of source, and review any publish or cloud submission command before approval.

Risk: Hybrid Genes can depend on third-party APIs and external domains.

Mitigation: Make third-party API use explicit in the phenotype network allowlist and avoid private, localhost, or undeclared service endpoints.

## Reference(s):

- [Rotifer Gene skill page](https://clawhub.ai/xiaoba-dev/skills/rotifer-gene)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground Repository](https://github.com/rotifer-protocol/rotifer-playground)
- [Gene Development](modules/dev.md)
- [Gene Security Audit](modules/audit.md)
- [Gene Fidelity Migration](modules/migration.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, TypeScript examples, JSON snippets, and checklist-style audit steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and may propose Rotifer CLI commands that read or write project files and optionally publish to Rotifer services.]

## Skill Version(s):

1.0.1 (source: server release evidence, SKILL.md frontmatter, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
