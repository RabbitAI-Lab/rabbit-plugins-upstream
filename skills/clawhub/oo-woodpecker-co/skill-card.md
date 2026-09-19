## Description:

Woodpecker.co helps agents inspect live connector schemas and read campaign, mailbox, prospect, and user data through an OOMOL-connected Woodpecker.co account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Woodpecker.co campaign settings, statistics, mailboxes, prospects, and active users through the OOMOL-connected CLI workflow. It is intended for account-scoped Woodpecker.co data access after the user has authenticated and connected the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the OOMOL CLI.

Mitigation: Verify the installer independently before execution, or use a pinned, signed, package-manager installation path.

Risk: The connected account may expose Woodpecker.co business data such as campaigns, prospects, mailboxes, and users.

Mitigation: Use an appropriately scoped Woodpecker.co account and retrieve only data needed for the user's request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-woodpecker-co)
- [Woodpecker.co Homepage](https://woodpecker.co/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return account-scoped Woodpecker.co data through the connected OOMOL CLI response format.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
