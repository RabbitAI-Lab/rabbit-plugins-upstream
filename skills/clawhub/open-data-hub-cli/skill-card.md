## Description:

Query Open Data Hub/NOI Techpark data through `odh`: Tourism, Mobility, traffic, A22, parking, EV charging, STA GTFS, and transit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Open Data Hub and NOI Techpark data with the `odh` CLI instead of scraping web pages. It guides discovery, traffic, mobility, tourism, A22, GTFS, and transit queries while emphasizing JSON output, source fields, warnings, freshness, and location checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party `odh` CLI installed from a Go module or Homebrew tap.

Mitigation: Review the disclosed CLI source and install path before use, pin the documented version, and apply normal approval controls for running installed commands.

Risk: Open Data Hub traffic, mobility, A22, and transit feeds can be stale, truncated, incomplete, or not live bulletins.

Mitigation: Prefer JSON output, inspect returned `warnings`, `source`, freshness, coverage, and truncation fields, and avoid claiming completeness or current conditions unless the returned data supports it.

Risk: Most practical data is South Tyrol / Autonomous Province of Bolzano, while some station rows may come from outside that area.

Mitigation: Verify record-level coordinates, origin, metadata, and stop IDs before making local or location-specific claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galjos/skills/open-data-hub-cli)
- [odh CLI repository](https://github.com/galjos/odh-cli)
- [Open Data Hub API](https://opendatahub.com/api/)
- [Open Data Hub datasets documentation](https://docs.opendatahub.com/en/latest/datasets.html)
- [Open Data Hub mobility getting started](https://docs.opendatahub.com/en/latest/howto/mobility/getstarted.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to request JSON output, inspect diagnostics, surface warnings, and run discovery commands before making claims.]

## Skill Version(s):

0.7.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
