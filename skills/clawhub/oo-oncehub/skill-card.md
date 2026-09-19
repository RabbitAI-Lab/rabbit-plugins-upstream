## Description:

Use this skill to search and read OnceHub booking pages, bookings, and event types through an OOMOL-connected OnceHub account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live OnceHub connector schemas and run read-only booking page, booking, and event type queries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer pipe commands for the oo CLI.

Mitigation: Install the oo CLI using a verified method and review the installer source before executing it.

Risk: OnceHub requests are brokered through OOMOL with server-side credentials.

Mitigation: Connect a OnceHub account only after confirming that OOMOL is trusted to broker requests and credentials.

Risk: Connector input and output schemas may change over time.

Mitigation: Inspect the live connector schema before constructing payloads for each action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-oncehub)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OnceHub Homepage](https://www.oncehub.com/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents run read-only OnceHub connector actions and receive JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
