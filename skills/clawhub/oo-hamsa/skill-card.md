## Description:

Hamsa (tryhamsa.com). Use this skill for searching and reading Hamsa data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Hamsa project, voice agent, text-to-speech voice, and paginated voice-agent list data through the oo CLI after connecting their OOMOL and Hamsa accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install oo from reviewed official release artifacts or package-manager instructions where possible, and verify integrity before executing installer content.

Risk: Account login and Hamsa connection steps may grant connector access to a user's OOMOL-connected Hamsa account.

Mitigation: Run login or account-connection steps only when the user intends to connect OOMOL to Hamsa and understands the account scope being granted.

## Reference(s):

- [Hamsa Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-hamsa)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Hamsa Homepage](https://tryhamsa.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
