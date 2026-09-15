## Description:

Use EODHD APIs through OOMOL's oo CLI to search instruments and retrieve market, macroeconomic, yield, account, and quote data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run authenticated EODHD API actions through OOMOL for market data lookup, quotes, macroeconomic indicators, yield rates, exchange listings, and account usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the oo CLI.

Mitigation: Use official, versioned installation instructions, inspect downloaded scripts, and verify checksums or signatures where available before execution.

Risk: The skill routes EODHD access through OOMOL-managed authentication.

Mitigation: Install only when the user accepts OOMOL as the intermediary for EODHD access and has connected the intended EODHD APIs account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-eodhd-apis)
- [EODHD APIs Homepage](https://eodhd.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON and include data plus meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
