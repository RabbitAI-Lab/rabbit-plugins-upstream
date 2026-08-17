## Description:

Use Signaturely through an OOMOL-connected account to read, create, and update Signaturely folder data via the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Signaturely action schemas and manage Signaturely folders through an OOMOL-connected account while preserving confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Signaturely folder state if run with an incorrect payload.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before create_folder or rename_folder.

Risk: The skill depends on OOMOL as the credential broker for the connected Signaturely account.

Mitigation: Complete oo CLI login and Signaturely connection setup only when the user trusts OOMOL for that account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-signaturely)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Signaturely homepage](https://signaturely.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema and run commands; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
