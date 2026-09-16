## Description:

NextDNS (nextdns.io) skill for searching and reading NextDNS data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list NextDNS profiles, inspect profile settings, review DNS analytics, and query DNS logs through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documented remote installer one-liners can execute unreviewed code during setup.

Mitigation: Do not let an agent run installer one-liners automatically; install the oo CLI only through a trusted, versioned, and verifiable method.

Risk: NextDNS logs can expose private browsing and device activity.

Mitigation: Limit log queries to the user's requested scope and avoid retaining or sharing DNS log output unnecessarily.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-next-dns)
- [NextDNS Homepage](https://nextdns.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides read-only NextDNS connector actions and first-time setup fallback steps.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
