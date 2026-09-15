## Description:

This skill helps agents discover Census Bureau datasets, inspect variables and groups, and query Census Data API datasets through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to search Census Bureau datasets, inspect schema details, and retrieve Census data through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the OOMOL CLI.

Mitigation: Use a verified, pinned installation method from the vendor instead of running remote installer scripts blindly.

Risk: Census queries are routed through OOMOL as an intermediary.

Mitigation: Use the skill only when OOMOL's account, billing, and data-handling practices are acceptable, and avoid sending confidential or identifying context in connector payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-census-bureau)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Census Bureau](https://www.census.gov)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector returns JSON data with execution metadata when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
