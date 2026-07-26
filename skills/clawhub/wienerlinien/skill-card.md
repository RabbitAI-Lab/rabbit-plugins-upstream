## Description: <br>
A skill for querying Vienna's public transport (Wiener Linien) real-time data including departures, disruptions, and elevator status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hjanuschka](https://clawhub.ai/user/hjanuschka) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and transit-focused agents use this skill to look up Vienna public transport departures, stop IDs, service disruptions, and elevator outages from public Wiener Linien data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires outbound requests to wienerlinien.at for normal operation. <br>
Mitigation: Run it only in environments where that public endpoint is permitted, and restrict outbound access to the required Wiener Linien domain when possible. <br>
Risk: Real-time public transport data can be unavailable, delayed, or incomplete. <br>
Mitigation: Treat results as live operational guidance and verify critical travel or accessibility decisions against official Wiener Linien channels. <br>


## Reference(s): <br>
- [Wiener Linien real-time API](https://www.wienerlinien.at/ogd_realtime) <br>
- [Wiener Linien stop reference CSV](https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and JSON-derived transit summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; normal use does not require credentials or private local data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
