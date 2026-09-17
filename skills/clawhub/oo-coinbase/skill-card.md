## Description:

This skill lets an agent read Coinbase Advanced Trade brokerage account data through the OOMOL oo CLI and a connected Coinbase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Coinbase account details and list accessible brokerage accounts from an OOMOL-connected Coinbase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands for the oo CLI.

Mitigation: Use a signed or pinned installation path and verify the installer source before running it.

Risk: The skill routes broadly to Coinbase while the documented actions are limited to read-only account lookups.

Mitigation: Use only the documented get_account and list_accounts actions unless updated evidence documents additional actions.

Risk: Coinbase account lookups pass through OOMOL-connected credentials.

Mitigation: Install only when using OOMOL as an intermediary is acceptable, and keep Coinbase access scoped to the documented read-only actions.

## Reference(s):

- [ClawHub Coinbase Skill](https://clawhub.ai/oomol/skills/oo-coinbase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Coinbase](https://www.coinbase.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution; documented actions are read-only account lookups.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
