## Description:

Marketstack (marketstack.com). Use this skill for Marketstack requests involving searching and reading market data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Marketstack end-of-day data, ticker profiles, available tickers, currencies, and exchanges through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that can execute local code.

Mitigation: Install the oo CLI only through a verified manual process, and review installer source or signatures before running it.

Risk: The skill depends on an OOMOL account connection model for Marketstack credentials.

Mitigation: Use it only when the user has intentionally connected Marketstack in OOMOL and is comfortable with server-side credential handling.

## Reference(s):

- [Marketstack homepage](https://marketstack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Marketstack skill page](https://clawhub.ai/oomol/skills/oo-marketstack)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include oo CLI schema-inspection commands, connector run commands, JSON request payloads, and summarized Marketstack results.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
