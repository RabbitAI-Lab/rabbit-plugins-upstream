## Description:

Finage gives an agent OOMOL-connected access to Finage market data for U.S. stock aggregates, latest quotes, latest trades, previous close data, snapshots, and symbol lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Finage market data through OOMOL's oo CLI, including U.S. stock bars, quotes, trades, snapshots, previous closes, and symbol lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts directly on the user's machine.

Mitigation: Do not let an agent run the curl-to-bash or PowerShell installer automatically; review the OOMOL CLI source or verified installation documentation and prefer a package-managed install where possible.

## Reference(s):

- [Finage homepage](https://finage.co.uk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-finage)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing oo CLI payloads; responses include data and an execution id.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
