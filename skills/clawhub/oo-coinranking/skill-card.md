## Description:

Coinranking (coinranking.com). Use this skill for Coinranking search and read-only cryptocurrency data requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Coinranking coin details, price history, global cryptocurrency market statistics, reference currencies, and keyword-based suggestions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands.

Mitigation: Verify the OOMOL installer source, version, and integrity before running the macOS, Linux, or Windows installer command.

Risk: Coinranking actions depend on an authenticated OOMOL-connected account.

Mitigation: Run routine read-only actions only after the oo CLI is installed, signed in, and connected; use setup or reconnection steps only after a matching command failure.

## Reference(s):

- [Coinranking Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-coinranking)
- [Coinranking Homepage](https://coinranking.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before running Coinranking actions; routine actions are read-only.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
