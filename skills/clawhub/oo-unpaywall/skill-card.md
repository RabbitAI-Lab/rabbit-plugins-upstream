## Description:

Unpaywall (unpaywall.org) supports searching and reading Unpaywall data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Unpaywall open-access metadata for DOIs and search Unpaywall articles by title through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a mutable remote installer directly in the shell.

Mitigation: Prefer a verified or documented oo CLI installation method before using the skill.

Risk: Unpaywall queries are routed through OOMOL as an intermediary.

Mitigation: Use the skill only when the OOMOL-connected account and data handling path are acceptable for the DOI or title queries being sent.

## Reference(s):

- [Unpaywall homepage](https://unpaywall.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unpaywall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
