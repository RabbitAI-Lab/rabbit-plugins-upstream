## Description:

Blocknative helps agents retrieve Blocknative gas-price estimates, Ethereum mainnet gas-price distributions, supported chains, and gas-oracle metadata through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query current Blocknative gas intelligence for Ethereum and supported chains without calling the Blocknative API directly. It is suited for read-only gas estimation, gas distribution lookup, chain discovery, and oracle metadata inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow documents remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, user-controlled process and review the installer before execution.

Risk: Blocknative access is mediated through an OOMOL-connected account.

Mitigation: Use the skill only when OOMOL handling the Blocknative connection is acceptable for the user's account and data policies.

Risk: Gas-price data is live network data and may change quickly.

Mitigation: Fetch the live action schema and current data at execution time, and avoid treating old responses as current estimates.

## Reference(s):

- [Blocknative homepage](https://www.blocknative.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blocknative)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution; actions documented in the artifact are read-only.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
