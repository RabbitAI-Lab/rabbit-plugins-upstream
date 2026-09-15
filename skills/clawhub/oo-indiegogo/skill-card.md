## Description:

Indiegogo (indiegogo.com). Use this skill for ANY Indiegogo request — searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and users use this skill to retrieve public Indiegogo creator details, crowdfunding project details, and active campaign lists through the OOMOL oo connector without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the setup path before installation, prefer verified releases or package-manager installs with integrity checks, and avoid running remote installer commands from an elevated shell.

Risk: Connector execution depends on the local oo CLI being installed and signed in to OOMOL.

Mitigation: Run connector actions only after confirming the oo CLI installation and authentication state, and use first-time setup only when commands fail for the documented reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-indiegogo)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Indiegogo](https://www.indiegogo.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions for public Indiegogo data; first-time setup may require oo CLI installation and OOMOL sign-in.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
