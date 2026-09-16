## Description:

Luno lets agents operate Luno through an OOMOL-connected account for account balances, market data, order lookup, and recent order listing via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Luno account, inspect balances and market data, and look up or list orders through OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes commands that execute downloaded installer scripts.

Mitigation: Prefer a verified or package-managed oo CLI install, inspect downloaded installers first, and do not run installer commands blindly.

Risk: The skill operates Luno through an OOMOL-connected account.

Mitigation: Install only if comfortable using OOMOL as an intermediary for Luno account access, and confirm the exact connector action and payload before authorizing state-changing use.

## Reference(s):

- [Luno homepage](https://www.luno.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
