## Description: <br>
Use DebugBundle for runtime error reporting, crash reporting, incident reporting, incident response, live app monitoring, and production monitoring focused on runtime failures, customer-facing incidents, and endpoint health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[debugbundle](https://clawhub.ai/user/debugbundle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and support engineers use DebugBundle to investigate production incidents, runtime errors, endpoint health, product analytics, and debug bundles, then guide evidence-based fixes through MCP and CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent access can expose incident, analytics, health-check, and management surfaces. <br>
Mitigation: Confirm the intended access before installation, use a scoped member token where possible, and avoid broad organization-wide queries unless the user explicitly requests them. <br>
Risk: Management operations may change monitoring, analytics, project, token, member, alert, webhook, billing, capture-policy, or improvement settings. <br>
Mitigation: Read existing settings first, explain the intended change, and perform mutations only when the user explicitly asks. <br>
Risk: Runtime evidence collection, probes, bundles, and analytics samples may include sensitive operational context. <br>
Mitigation: Use bounded queries, short-lived scoped probes, existing redaction and retention controls, and never print credential values or raw sensitive payloads. <br>


## Reference(s): <br>
- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp) <br>
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics) <br>
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics) <br>
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools) <br>
- [ClawHub DebugBundle skill page](https://clawhub.ai/debugbundle/skills/debugbundle) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and MCP or CLI action guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide read and mutation workflows across incidents, health checks, analytics, project settings, and management surfaces; credential values and sensitive payloads should not be printed.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
