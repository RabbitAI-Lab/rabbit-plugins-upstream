## Description: <br>
Clinical-facility edition of iaiops for hospital facilities monitoring and analysis across BACnet/IP BMS points, Modbus medical-gas and meter devices, OPC-UA plant SCADA, and clinical safety checks for isolation-room pressure, medical gas, and operating-room environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facilities engineers, clinical engineering teams, and agent developers use this skill to inspect hospital BMS, medical-gas, metering, and SCADA signals, summarize safety-relevant conditions, and triage downtime or alarm issues. It is read-first, but its documented BACnet write path requires management-of-change controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release describes the edition as read-only while also documenting a BACnet write tool for high-impact clinical building controls. <br>
Mitigation: Treat BACnet writes as high-risk operations; keep dry-run behavior enabled by default and require authorization, management-of-change approval, pre-change values, rollback planning, and external change controls before any real write. <br>
Risk: Hospital HVAC, isolation-room pressure, and medical-gas systems can affect patient safety if recommendations or actions are wrong. <br>
Mitigation: Review findings with qualified facility, infection-control, and clinical engineering staff, and defer to site procedures, NFPA 99 alarm panels, and other authoritative local systems before operational action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with inline commands, tool plans, analysis summaries, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include worst-first clinical facility findings, cited point readings, dry-run write plans, and approval or rollback guidance.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
