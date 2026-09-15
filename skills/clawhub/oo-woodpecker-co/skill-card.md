## Description:

Woodpecker.co (woodpecker.co). Use this skill for ANY Woodpecker.co request — searching and reading data. Whenever a task involves Woodpecker.co, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Woodpecker.co action schemas and read campaigns, campaign statistics, mailboxes, prospects, and active users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Install the oo CLI through verified official release steps, inspect downloaded scripts before execution, and avoid running installer commands with elevated privileges.

Risk: The skill depends on local oo CLI authentication and an active Woodpecker.co connection.

Mitigation: Run setup only after an auth or connection failure, then use the documented OOMOL login and Woodpecker.co connection flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-woodpecker-co)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Woodpecker.co](https://woodpecker.co/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads data through the oo CLI and returns connector responses as JSON when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
