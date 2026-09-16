## Description:

LeadBoxer (leadboxer.com). Use this skill for ANY LeadBoxer request - searching and reading data. Whenever a task involves LeadBoxer, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate LeadBoxer through an OOMOL-connected account for read-only domain and IP enrichment. The skill inspects live action schemas before submitting JSON payloads and returns organization, firmographic, network, and geolocation lookup results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing third-party code on the user's machine.

Mitigation: Review setup commands before use, prefer a trusted version-pinned oo CLI package or verified release, and avoid curl-to-bash or PowerShell iex installation unless that execution risk is accepted.

Risk: LeadBoxer access depends on an OOMOL-connected account and server-side credentials.

Mitigation: Run connection or authentication setup only after an oo CLI command fails with the matching auth, connection, scope, or credential error.

## Reference(s):

- [LeadBoxer homepage](https://www.leadboxer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-leadboxer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-only LeadBoxer connector actions for domain and IP enrichment through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
