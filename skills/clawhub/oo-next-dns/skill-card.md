## Description:

This skill helps agents search and read NextDNS profile settings, setup details, analytics, and logs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect NextDNS profiles, analytics, blocking reasons, status, and DNS logs through the OOMOL oo CLI after their account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes mutable remote installer commands that execute downloaded shell or PowerShell scripts without a pinned version or integrity check.

Mitigation: Review the installer source before execution, prefer a verified package or inspected release artifact when available, and run setup commands only after an auth or connection failure requires them.

## Reference(s):

- [NextDNS homepage](https://nextdns.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-next-dns)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns read-only NextDNS data when commands are run.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
