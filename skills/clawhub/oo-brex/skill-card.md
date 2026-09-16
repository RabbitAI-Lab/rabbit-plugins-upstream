## Description:

Use this skill for Brex (brex.com) requests to search and read data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and finance operations users use this skill to inspect Brex company, user, budget, card account, expense, and settled transaction data through an authenticated OOMOL-connected Brex account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup recommends remote shell or PowerShell installer commands.

Mitigation: Use a verified package, pinned release, checksum, or reviewed installer before installing the oo CLI.

Risk: The skill can read company financial data from an authenticated Brex connection.

Mitigation: Use least-privileged Brex credentials and install only when the publisher and connected account are trusted.

Risk: The trigger is broad for Brex-related requests.

Mitigation: Review intended Brex actions before use and require explicit confirmation for any future write or destructive connector action.

## Reference(s):

- [ClawHub Brex Skill](https://clawhub.ai/oomol/skills/oo-brex)
- [Brex Homepage](https://www.brex.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running Brex read actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
