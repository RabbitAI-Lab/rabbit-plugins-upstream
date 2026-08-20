## Description:

Countly connector skill for searching and reading Countly data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Countly app metadata, current-user details, dashboard analytics, event analytics, session analytics, and app lists through the oo CLI without handling raw Countly tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses OOMOL as the broker for the Countly connection and may require installing or signing in to the oo CLI.

Mitigation: Confirm that the user accepts OOMOL-brokered Countly access and only perform first-time CLI or connection setup when an authentication, connection, scope, credential, app, or billing error requires it.

Risk: Future connector actions tagged write or destructive could modify or remove Countly data.

Mitigation: Fetch the live connector schema before execution and require explicit user confirmation of the exact payload and effect before any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-countly)
- [Countly Homepage](https://countly.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema guidance, and JSON-shaped Countly action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
