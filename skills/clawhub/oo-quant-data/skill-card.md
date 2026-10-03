## Description:

Quant Data (quantdata.us) helps agents search and read Quant Data market datasets through the OOMOL `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Quant Data market datasets, including dark-pool activity, equity prints, options order flow, dealer exposure, volatility skew, IV rank, gainers and losers, and ticker-tagged news through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute a remotely fetched installer for the oo CLI.

Mitigation: Use the official install guide, inspect or verify installer artifacts where possible, and connect only the Quant Data account intended for this skill.

Risk: Actions rely on the user's connected OOMOL account and Quant Data access state.

Mitigation: Run setup, sign-in, or connection steps only after an auth, scope, credential, app, or billing error indicates they are needed.

Risk: Incorrect payloads could produce failed or misleading data queries.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each `oo connector run` payload.

## Reference(s):

- [Quant Data homepage](https://quantdata.us/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quant-data)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
