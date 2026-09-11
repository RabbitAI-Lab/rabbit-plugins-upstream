## Description:

Query Open Data Hub/NOI Techpark data through `odh`: Tourism, Mobility, traffic, A22, parking, EV charging, STA GTFS, and transit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galjos](https://clawhub.ai/user/galjos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Open Data Hub and NOI Techpark datasets through the `odh` CLI or MCP surface, especially for South Tyrol mobility, traffic, tourism, parking, EV charging, A22, STA GTFS, and transit questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run a third-party `odh` CLI.

Mitigation: Confirm the CLI source and installation path are acceptable before installation, and run the documented `odh version` and `odh doctor --timeout 10s` checks before use.

Risk: Public traffic, mobility, and transit feeds can be stale, incomplete, truncated, or non-live.

Mitigation: Use structured output, report returned warnings and provenance fields, and check freshness, coverage, truncation, and source details before making operational claims.

## Reference(s):

- [Open Data Hub CLI source](https://github.com/galjos/odh-cli)
- [Open Data Hub API](https://opendatahub.com/api/)
- [Open Data Hub datasets documentation](https://docs.opendatahub.com/en/latest/datasets.html)
- [Open Data Hub mobility getting started](https://docs.opendatahub.com/en/latest/howto/mobility/getstarted.html)
- [ClawHub skill page](https://clawhub.ai/galjos/skills/open-data-hub-cli)
- [ClawHub publisher profile](https://clawhub.ai/user/galjos)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented parsing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to prefer structured `odh` JSON output, surface warnings and provenance fields, and check freshness, coverage, and truncation before making claims.]

## Skill Version(s):

0.7.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
