## Description:

Kaleido (kaleido.io) enables agents to search and read Kaleido data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Kaleido consortia, memberships, environments, nodes, and services from an OOMOL-connected account. It is intended for read-oriented status checks and data lookups through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of internet installer scripts in a shell.

Mitigation: Review the installer path first and prefer an official verifiable installation method for the oo CLI before running installer commands.

Risk: Kaleido access depends on an OOMOL-connected account and valid scoped credentials.

Mitigation: Use the documented authentication and connection recovery steps only after a command fails with an auth, missing-scope, expired-credential, or app-connection error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kaleido)
- [Kaleido Homepage](https://www.kaleido.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
