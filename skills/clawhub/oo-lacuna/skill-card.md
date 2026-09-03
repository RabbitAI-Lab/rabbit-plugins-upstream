## Description:

Lacuna (lacuna.tiptreesystems.com). Use this skill for searching and reading Lacuna research data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research workflows use this skill to search Lacuna's machine-learning research map and retrieve source-linked context for papers, directions, authors, institutions, venues, and generated hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Install only after trusting OOMOL and the oo CLI distribution path; prefer verified release documentation or review the installer before running curl-to-shell or PowerShell installer commands.

Risk: Future write or destructive Lacuna connector actions could change or remove data if approved without reviewing the payload.

Mitigation: Review the live connector schema, exact payload, and intended effect before approving any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lacuna)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Lacuna Homepage](https://lacuna.tiptreesystems.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Lacuna connector schemas before each action; normal actions are read and search focused.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
