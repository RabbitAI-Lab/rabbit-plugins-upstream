## Description: <br>
Query Open Data Hub/NOI Techpark data through `odh`: Tourism, Mobility, traffic, A22, parking, EV charging, STA GTFS, and transit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galjos](https://clawhub.ai/user/galjos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query Open Data Hub and NOI Techpark data with the `odh` CLI instead of scraping pages. It supports discovery and retrieval workflows for tourism, mobility, traffic, A22, parking, EV charging, STA GTFS, and transit data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an external `odh` CLI that can make network queries to Open Data Hub APIs. <br>
Mitigation: Install only if the upstream CLI source is acceptable, verify `odh v0.6.1+`, and run `odh doctor` before relying on results. <br>
Risk: Open data responses may be stale, incomplete, outside the expected geography, or include warnings that affect interpretation. <br>
Mitigation: Check freshness, warnings, source fields, provenance fields, and record-level coordinates or metadata before presenting conclusions. <br>
Risk: Some feeds are not live bulletins, so empty or stale results can be mistaken for current real-world status. <br>
Mitigation: Phrase results as what the queried feed returned, surface stale/source warnings, and avoid claiming roads or transit are clear solely from empty feed responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/galjos/skills/open-data-hub-cli) <br>
- [Open Data Hub API](https://opendatahub.com/api/) <br>
- [Open Data Hub datasets documentation](https://docs.opendatahub.com/en/latest/datasets.html) <br>
- [Open Data Hub mobility getting started](https://docs.opendatahub.com/en/latest/howto/mobility/getstarted.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to use `--json` or `--format json` for parseable CLI output and to treat stderr as diagnostics.] <br>

## Skill Version(s): <br>
0.6.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
