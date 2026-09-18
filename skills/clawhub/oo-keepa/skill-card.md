## Description:

Keepa lets an agent query Amazon product, deal, category, seller, product-history, snapshot, and token-status data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to handle Keepa-related ecommerce requests by inspecting connector schemas and running Keepa actions for Amazon product discovery, deal filtering, category lookup, seller snapshots, price and rank history, and token status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of remote installer scripts.

Mitigation: Use verified installation instructions or inspect and download the installer before executing it.

Risk: Keepa queries are routed through OOMOL-managed credentials.

Mitigation: Install only when use of OOMOL as an intermediary is acceptable, and honor requests for direct Keepa API access instead.

## Reference(s):

- [Keepa homepage](https://keepa.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Keepa skill page](https://clawhub.ai/oomol/skills/oo-keepa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
