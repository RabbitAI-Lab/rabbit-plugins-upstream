## Description: <br>
Query Open Data Hub and NOI Techpark data through `odh`, covering Tourism, Mobility, traffic, A22, parking, EV charging, STA GTFS, and transit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galjos](https://clawhub.ai/user/galjos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query Open Data Hub and NOI Techpark public datasets through the `odh` CLI instead of scraping web pages. It is especially useful for South Tyrol tourism, mobility, traffic, parking, EV charging, GTFS, and transit data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may cause an agent host to install and execute the third-party `odh` Go command-line tool. <br>
Mitigation: Install only in environments that intend to use `odh`; review the CLI package and version before enabling execution. <br>
Risk: The CLI may make network requests to open-data services and return stale, truncated, or non-live public data. <br>
Mitigation: Use the skill's freshness filters, warning fields, source/provenance fields, timeouts, and current-notice checks before presenting results as current. <br>


## Reference(s): <br>
- [Open Data Hub API](https://opendatahub.com/api/) <br>
- [Open Data Hub Datasets](https://docs.opendatahub.com/en/latest/datasets.html) <br>
- [Open Data Hub Mobility Getting Started](https://docs.opendatahub.com/en/latest/howto/mobility/getstarted.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/galjos/skills/open-data-hub-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented output instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes JSON output flags, diagnostics handling, returned source fields, warnings, freshness checks, and bounded timeouts.] <br>

## Skill Version(s): <br>
0.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
