## Description:

Concord lets an agent search and read Concord data through the OOMOL-connected oo CLI instead of calling the Concord API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect accessible Concord users, organizations, folders, and agreements through an authenticated OOMOL account connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires OOMOL to broker access to the user's Concord account and can read Concord organizations, folders, and agreements available to that account.

Mitigation: Install only when that access model is acceptable, connect the minimum needed Concord account, and review returned data before sharing it outside the authorized workflow.

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Avoid pipe-to-shell installation; use an official pinned package or download the installer and verify its signature or checksum before execution.

Risk: The release security verdict is suspicious and recommends review before use.

Mitigation: Perform a security review before deployment and keep setup, authentication, and billing recovery steps limited to cases where the corresponding command failure occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-concord)
- [Concord Homepage](https://www.concord.app/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for running oo CLI connector schema and run commands; action responses are JSON when --json is used.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
