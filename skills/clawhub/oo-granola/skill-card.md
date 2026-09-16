## Description:

Granola (granola.ai). Use this skill for ANY Granola request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Granola meetings, notes, folders, summaries, and eligible transcripts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI from a trusted, versioned, verifiable source and review the setup path before use.

Risk: Connecting Granola through OOMOL-mediated access can expose meeting notes and transcripts to the connector workflow.

Mitigation: Connect Granola only when the user accepts that access, and keep transcript retrieval limited to eligible and intended meetings.

Risk: Granola transcript and folder access can depend on paid-plan eligibility.

Mitigation: Check plan eligibility and handle billing or access errors before retrying failed transcript or folder requests.

## Reference(s):

- [ClawHub Granola Skill](https://clawhub.ai/oomol/skills/oo-granola)
- [Granola Homepage](https://www.granola.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before forming requests; read access can include meeting notes, summaries, folders, and eligible transcripts.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
