## Description:

Blocknative (blocknative.com). Use this skill for ANY Blocknative request: searching and reading gas-price and gas-oracle data through an OOMOL-connected Blocknative account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Blocknative gas-price estimates, Ethereum mainnet gas-price distributions, supported chains, and gas-oracle metadata through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer commands that can execute local code.

Mitigation: Install the oo CLI only from a pinned, verifiable release or trusted package manager; avoid curl-to-bash or irm-to-iex unless the installer path is trusted.

Risk: Connector actions depend on the user's OOMOL account connection and live Blocknative access.

Mitigation: Run setup and connection steps only after an auth or connection failure, then use the live connector schema before sending any payload.

## Reference(s):

- [Blocknative homepage](https://www.blocknative.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blocknative)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI connector schemas before running Blocknative read actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
