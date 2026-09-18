## Description:

Provides agents with Grafana Cloud read access through the OOMOL grafana_cloud connector for billed usage, stack connectivity, available regions, and stack listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to answer Grafana Cloud account questions with read-only actions for billed usage, stack connectivity, available regions, and stack inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes unverified remote script execution for installing the required oo CLI.

Mitigation: Review the installer source and prefer a pinned, signed, or package-manager installation before using the skill.

Risk: Future connector actions could introduce write or destructive Grafana Cloud operations.

Mitigation: Keep use to the listed read-only actions and inspect the exact schema and payload before approving any future write or destructive action.

## Reference(s):

- [Grafana Cloud homepage](https://grafana.com/products/cloud/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-grafana-cloud)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Grafana Cloud actions are listed; inspect live schemas before constructing payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
