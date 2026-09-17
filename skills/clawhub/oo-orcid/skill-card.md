## Description:

ORCID (orcid.org). Use this skill for ANY ORCID request: searching and reading public ORCID data through OOMOL's ORCID connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public ORCID researcher records, retrieve public works summaries, and search ORCID records with Solr query syntax through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source first, prefer a signed or checksum-verified oo CLI release or trusted package manager, and avoid running curl|bash or irm|iex in a privileged shell.

Risk: The skill depends on OOMOL account authentication and an ORCID connection before actions can run.

Mitigation: Run setup steps only after an auth or connection error, and use the OOMOL connection page to refresh expired or missing ORCID credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-orcid)
- [ORCID homepage](https://orcid.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/orcid.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before sending JSON payloads to read-only ORCID actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
