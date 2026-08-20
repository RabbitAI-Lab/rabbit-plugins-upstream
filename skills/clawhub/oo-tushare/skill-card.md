## Description:

Use this skill to search and read Tushare data through Tushare (tushare.pro) instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Tushare market data through an OOMOL-connected account, including A-share stock basics, quotes, daily indicators, adjustment factors, shareholder trades, trade calendars, and generic Tushare data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use may require installing the oo CLI and signing in to an OOMOL account before the agent can query Tushare.

Mitigation: Review the CLI installation step and OOMOL account connection before approving setup commands.

Risk: Tushare access depends on an OOMOL-connected account and may stop on connection, credential, scope, or billing errors.

Mitigation: Use the documented first-time setup and billing guidance only after a matching command failure occurs.

## Reference(s):

- [Tushare homepage](https://tushare.pro)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tushare)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented connector commands that inspect the live action schema before running Tushare queries.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
