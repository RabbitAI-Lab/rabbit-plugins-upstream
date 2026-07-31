## Description: <br>
Vendor-neutral, governed, read-only energy/substation telecontrol data tap for monitor-direction telemetry over IEC 60870-5-104, DNP3 / IEEE 1815, and IEC 61850 MMS, plus cross-protocol Industrial-AIOps analysis tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and utility telemetry engineers use this skill to route agent tasks to read-only substation and utility SCADA telemetry checks, protocol status reads, integrity polls, model browsing, data-quality analysis, and compliance self-assessment. It is intended for authorized monitoring and diagnosis, not control or write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized or accidental connection to production utility telemetry systems could create operational network traffic even when tools are read-only. <br>
Mitigation: Use only approved endpoints, verify authorization before installation, and test against non-production or approved systems first. <br>
Risk: Credentials or target connection details could be mishandled during setup. <br>
Mitigation: Store credentials only in the documented secret store or environment path and avoid placing secrets in chat or plain configuration. <br>
Risk: DNP3 and IEC 61850 paths may require manual or Docker verification where native protocol libraries are not covered by hosted CI. <br>
Mitigation: Re-verify those monitor paths in an approved Linux or Docker environment before relying on them for operational monitoring. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/zw008/skills/iaiops-energy) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Analysis] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing routing, installation, configuration, protocol-read, and safety guidance; live tool results are monitor-only and should not expose secrets.] <br>

## Skill Version(s): <br>
0.1.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
