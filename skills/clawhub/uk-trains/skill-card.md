## Description: <br>
Query UK National Rail live departure boards, arrivals, delays, and train services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jabbslad](https://clawhub.ai/user/jabbslad) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to check UK National Rail departures, arrivals, delays, platforms, and train services for GB stations. It supports live railway lookups through National Rail Darwin and Huxley2 APIs when a National Rail token is configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A National Rail API token could be exposed through source control, shell history, logs, or an untrusted configured endpoint. <br>
Mitigation: Use a dedicated, revocable token; keep it out of source control and logs; avoid setting HUXLEY_URL unless the endpoint is trusted. <br>
Risk: Live train data depends on external rail APIs and may be unavailable, delayed, or incomplete. <br>
Mitigation: Present results as live service lookups and preserve service alerts, cancellation reasons, and delay reasons returned by the API. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jabbslad/skills/uk-trains) <br>
- [National Rail OpenLDBWS Registration](https://realtime.nationalrail.co.uk/OpenLDBWSRegistration/) <br>
- [National Rail Darwin OpenLDBWS Endpoint](https://lite.realtime.nationalrail.co.uk/OpenLDBWS/ldb12.asmx) <br>
- [Huxley2 Default Endpoint](https://huxley2.azurewebsites.net) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON from command-line queries, plus compact Markdown or chat text for user-facing train updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NATIONAL_RAIL_TOKEN for live Darwin or Huxley2 train lookups; HUXLEY_URL can override the default Huxley2 endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
