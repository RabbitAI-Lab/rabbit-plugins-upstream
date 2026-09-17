## Description:

MotherDuck helps agents administer MotherDuck through the OOMOL-connected oo CLI, including account, user, token, and Duckling configuration actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect MotherDuck connector schemas and run structured read, write, and destructive admin actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and delete MotherDuck users and access tokens.

Mitigation: Require explicit user confirmation for token creation, token deletion, user deletion, user creation, and configuration changes before running the action.

Risk: The first-time setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Review or verify the oo CLI installer before executing it, and install the skill only when MotherDuck administration through OOMOL is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mother-duck)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [MotherDuck Homepage](https://motherduck.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL MotherDuck Connection](https://console.oomol.com/app-connections?provider=mother_duck)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before constructing payloads and to require confirmation for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: release evidence and metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
