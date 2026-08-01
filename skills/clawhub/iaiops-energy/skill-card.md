## Description: <br>
Provides read-only energy and substation telecontrol telemetry over IEC 60870-5-104, DNP3/IEEE 1815, and IEC 61850 MMS, with Industrial-AIOps analysis for authorized utility monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, utility engineers, and authorized operations teams use this skill to monitor substation telemetry, inspect protocol link status, run read-only interrogations or integrity polls, and analyze operational data quality across supported energy protocols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized use on operational utility or substation networks could create safety, compliance, or service risks even though the skill is read-only. <br>
Mitigation: Install and run the skill only for systems the operator is authorized to monitor, and confirm target scope before connecting to live equipment. <br>
Risk: Status checks, interrogations, integrity polls, and model reads generate real traffic on operational links. <br>
Mitigation: Start with low-impact status or directory tools, then proceed to broader reads only after confirming the endpoint, protocol, and operational window. <br>
Risk: Credentials or endpoint details could be mishandled during setup. <br>
Mitigation: Keep credentials in the documented secret mechanism, pass runtime configuration through environment or config files, and avoid placing secrets in prompts or chat history. <br>
Risk: The release depends on external pip packages and protocol client libraries. <br>
Mitigation: Review package provenance and install only the protocol extras required for the monitored environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-energy) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets; MCP tool results may be structured text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Monitor-only workflows; no control or operate actions are exposed.] <br>

## Skill Version(s): <br>
0.1.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
