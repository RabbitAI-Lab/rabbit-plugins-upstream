## Description:

timelink provides read-oriented access to Timelink data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, list, and fetch Timelink clients, companies, projects, services, users, tokens, and time entries from a connected Timelink account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official, versioned, signed, or checksum-verified oo CLI installer and review setup commands before execution.

Risk: Using the skill requires OOMOL-mediated access to Timelink data.

Mitigation: Install only when OOMOL is an acceptable intermediary for the intended Timelink account and data.

Risk: Account connection and CLI login can make persistent changes to the local environment.

Mitigation: Run setup only after an authentication or connection error, and use an account scoped to the intended Timelink access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timelink)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Timelink homepage](https://timelink.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Timelink get and list actions; setup guidance may require oo CLI authentication and a connected Timelink account.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
