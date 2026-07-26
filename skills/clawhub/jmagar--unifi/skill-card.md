## Description: <br>
Query and monitor UniFi network via local gateway API (Cloud Gateway Max / UniFi OS). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and network administrators use this skill to query local UniFi gateway data for device status, active clients, site health, top applications, alerts, and dashboard-style network summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard command can retain sensitive network inventory and raw debug data locally. <br>
Mitigation: Inspect or remove generated inventory and debug files after use, and avoid running the dashboard on systems where local retention of network details is not acceptable. <br>
Risk: The skill needs UniFi credentials and local gateway access. <br>
Mitigation: Use a dedicated least-privilege UniFi account where possible and restrict permissions on the credentials file. <br>
Risk: TLS certificate verification is disabled by default for UniFi API calls. <br>
Mitigation: Review this behavior before use on sensitive networks and adapt the scripts to verify the gateway certificate if required by local policy. <br>


## Reference(s): <br>
- [UniFi read-only endpoints](references/unifi-readonly-endpoints.md) <br>
- [UniFi Controller API community reference](https://ubntwiki.com/products/software/unifi-controller/api) <br>
- [ClawHub skill page](https://clawhub.ai/jmagar/skills/unifi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Human-readable terminal tables and dashboards, with optional raw JSON output for supported commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq, local UniFi gateway network access, and a local UniFi credentials file.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
