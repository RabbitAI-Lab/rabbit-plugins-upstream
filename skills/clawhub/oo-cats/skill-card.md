## Description:

CATS helps agents search and read CATS recruiting data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, recruiting operations teams, and authorized agents use this skill to retrieve, list, and search CATS candidates, companies, jobs, and site information from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute remote installer scripts.

Mitigation: Install the oo CLI only from a verified official package or reviewed installer, and avoid letting an agent run curl-to-shell or PowerShell iex installer commands.

Risk: The oo CLI can access CATS through the connected account, and the tool permission is broader than the listed read actions require.

Mitigation: Install only if OOMOL is trusted, and use an OOMOL/CATS account limited to the read access needed for candidates, companies, jobs, and site information.

## Reference(s):

- [CATS homepage](https://catsone.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub CATS skill](https://clawhub.ai/oomol/skills/oo-cats)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from CATS through the oo CLI; action payloads must follow the live connector schema.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
