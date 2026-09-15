## Description:

Humaans helps agents search and read Humaans people records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve current person details, individual person records, token scope information, and filtered people lists from Humaans after the account is connected through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use verified official installation steps with checksum or signature validation instead of running the curl-to-bash or Invoke-Expression commands as written.

Risk: Using the skill requires trusting OOMOL as an intermediary for Humaans reads and granting Humaans account scopes.

Mitigation: Review OOMOL's role and the requested Humaans scopes before connecting the account, and limit access to the minimum scopes needed.

## Reference(s):

- [Humaans homepage](https://humaans.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Humaans connection](https://console.oomol.com/app-connections?provider=humaans)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are returned as JSON.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
