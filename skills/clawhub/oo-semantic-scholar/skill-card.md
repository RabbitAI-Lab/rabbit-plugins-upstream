## Description:

Semantic Scholar helps agents search and retrieve paper, author, citation, reference, snippet, and recommendation data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and agents use this skill to search Semantic Scholar and retrieve publication metadata, author records, citation and reference lists, snippets, and paper recommendations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags unverified pipe-to-shell installer commands.

Mitigation: Review setup steps before use and prefer official, pinned, verifiable installation steps for the oo CLI.

Risk: The security evidence flags broad routing of Semantic Scholar searches through OOMOL.

Mitigation: Use the connector only for intended Semantic Scholar tasks, inspect the live action schema before execution, and confirm setup or authentication actions yourself.

## Reference(s):

- [Semantic Scholar homepage](https://www.semanticscholar.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-semantic-scholar)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
