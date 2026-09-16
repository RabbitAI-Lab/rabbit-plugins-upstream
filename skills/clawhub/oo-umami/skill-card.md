## Description:

Umami connects an agent to Umami analytics through the OOMOL-connected oo CLI for searching and reading website, metric, pageview, realtime, statistics, and event data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect Umami action schemas and retrieve read-only analytics data from websites connected to their OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands.

Mitigation: Prefer an official package manager or a downloaded, pinned installer with checksum or signature verification before installing the oo CLI.

Risk: Authentication, connection, or billing failures can block Umami actions.

Mitigation: Run setup, connection, or billing steps only after a matching command failure and keep normal analytics actions scoped to the configured OOMOL account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-umami)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Umami homepage](https://umami.is)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal action results are JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
