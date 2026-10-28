## Description:

Helps developers build, audit, and migrate Rotifer Genes using phenotype schemas, security checks, and the Rotifer CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and test Rotifer Genes, check them before publication, and migrate their fidelity from Wrapped to Hybrid or Native.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login, publishing, and cloud submission can affect accounts or public registry state.

Mitigation: Review and approve these actions before running them.

Risk: Suggested CLI commands or overwrites can change project files; installing the CLI fetches a package.

Mitigation: Review file changes and commands first, and use the documented pinned CLI version.

Risk: Publishing a Gene can expose credentials or sensitive project details.

Mitigation: Run the documented four-layer audit and inspect upload content before publication.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground repository (listed in skill manifest)](https://github.com/rotifer-protocol/rotifer-playground)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers Gene development, security audits, and fidelity migration.]

## Skill Version(s):

1.0.4 (source: skill frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
