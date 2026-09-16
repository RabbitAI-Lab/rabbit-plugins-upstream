## Description:

Provides agent guidance for querying Tushare through the OOMOL oo CLI, including schema inspection, read actions, setup fallback, and normalized JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Tushare market data through an OOMOL-connected account, including A-share listings, daily quotes, valuation indicators, adjustment factors, shareholder trades, trading calendars, and generic Tushare API queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can lead an agent to run unverified remote installer commands with the user's account permissions.

Mitigation: Review the skill before installation, avoid automatic execution of remote installer commands, and prefer a verified, versioned oo CLI installation path with checksum or signature validation.

Risk: The skill depends on an OOMOL-connected account and Tushare connector state for live data access.

Mitigation: Confirm account login, connector setup, credential status, and billing state directly when an action fails for authentication, scope, credential, app readiness, or credit reasons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tushare)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Tushare homepage](https://tushare.pro)
- [OOMOL app connection for Tushare](https://console.oomol.com/app-connections?provider=tushare)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include oo CLI commands, schema-based JSON payloads, normalized tabular data summaries, and setup guidance for authentication, connector status, or billing failures.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
