## Description:

Trendshift lets agents query repository trend data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Trendshift and GitHub Trending snapshots, ranked daily, weekly, monthly, and yearly repository trends, and engagement spike data through an OOMOL-connected Trendshift account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected Trendshift account.

Mitigation: Review the CLI install script and complete login or connection steps only when OOMOL is an intended credential-handling intermediary for Trendshift reads.

Risk: Connector requests can fail when authentication, Trendshift connection scopes, app readiness, or account credit are missing.

Mitigation: Run setup, reconnection, or billing steps only after a command fails with the matching error.

Risk: A stale or guessed payload can mismatch the connector contract.

Mitigation: Inspect the live action schema with oo connector schema before constructing action payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-trendshift)
- [Trendshift Homepage](https://trendshift.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; actions should be run only after inspecting the live action schema.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
