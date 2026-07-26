## Description: <br>
Iaiops Energy routes agents to a governed, read-only MCP server for utility and substation telemetry over IEC 60870-5-104, DNP3 / IEEE 1815, and IEC 61850 MMS, plus related Industrial-AIOps diagnostics and analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation engineers, and authorized utility operators use this skill to route substation telemetry, SCADA gateway, RTU, and IED monitoring tasks to read-only MCP tools and related diagnostic guidance. It is intended for monitoring and analysis, not breaker operation, setpoints, relay setting changes, or other control actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting to production telecontrol systems without authorization or preparation can create operational risk even when tools are read-only. <br>
Mitigation: Install only in an authorized utility or lab environment and verify read-only behavior before connecting to production gear. <br>
Risk: Target credentials or configuration details could be exposed if placed in chat or plain configuration. <br>
Mitigation: Keep credentials in the documented secret manager path and pass only non-secret target configuration through the skill. <br>
Risk: DNP3 and IEC 61850 monitor paths are described as manually or Docker verified rather than continuously CI-gated. <br>
Mitigation: Re-verify those protocol paths in the intended runtime environment before relying on them for production monitoring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-energy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agent routing to read-only MCP tools for telemetry reads, link checks, integrity polls, model browsing, and analysis.] <br>

## Skill Version(s): <br>
0.1.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
