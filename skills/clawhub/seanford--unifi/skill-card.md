## Description: <br>
Query and monitor UniFi network via local gateway API (Cloud Gateway Max / UniFi OS). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network operators, developers, and home lab administrators use this skill to inspect UniFi device status, connected clients, site health, traffic application usage, and recent alerts from a local UniFi gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Admin credentials and internal network details may be exposed because the scripts store credentials locally and dashboard runs save network inventory data to disk. <br>
Mitigation: Use a least-privilege local UniFi account, restrict credential file permissions, and avoid sharing generated dashboard or JSON outputs. <br>
Risk: The scripts disable TLS certificate verification for UniFi gateway requests, which can expose credentials if the gateway connection is spoofed or intercepted. <br>
Mitigation: Run only on trusted local networks, verify the configured gateway address before use, and review the TLS behavior before installation. <br>


## Reference(s): <br>
- [UniFi Local Gateway read-only API endpoints](references/unifi-readonly-endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/unifi) <br>
- [Publisher profile](https://clawhub.ai/user/seanford) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, tables, and optional JSON output from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; commands query a configured local UniFi gateway.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
