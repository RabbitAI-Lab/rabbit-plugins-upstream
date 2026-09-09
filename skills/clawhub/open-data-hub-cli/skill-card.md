## Description:

Query Open Data Hub/NOI Techpark data through `odh`: Tourism, Mobility, traffic, A22, parking, EV charging, STA GTFS, and transit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Open Data Hub and NOI Techpark data through the `odh` CLI or MCP surface, while preserving source, freshness, warning, and caveat information in answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party `odh` CLI, which may require review in environments that restrict external Go tools.

Mitigation: Review the `odh` CLI source or release provenance and install only an approved version before deployment.

Risk: Open Data Hub responses can include stale, incomplete, or geographically broad records.

Mitigation: Preserve source, freshness, warning, caveat, and coordinate metadata before making current or local-status claims.

## Reference(s):

- [Skill release page](https://clawhub.ai/galjos/skills/open-data-hub-cli)
- [Open Data Hub CLI repository](https://github.com/galjos/odh-cli)
- [Open Data Hub API](https://opendatahub.com/api/)
- [Open Data Hub datasets documentation](https://docs.opendatahub.com/en/latest/datasets.html)
- [Open Data Hub mobility getting started](https://docs.opendatahub.com/en/latest/howto/mobility/getstarted.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the third-party `odh` CLI v0.6.2 or later; supports MCP server mode through `odh mcp serve`.]

## Skill Version(s):

0.6.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
