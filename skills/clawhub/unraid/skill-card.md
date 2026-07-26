## Description: <br>
Query and monitor Unraid servers via the GraphQL API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and homelab administrators use this skill to ask an agent for Unraid server status, disk health, logs, shares, containers, VMs, and monitoring commands backed by the Unraid GraphQL API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query sensitive Unraid infrastructure data, including system status, logs, storage, containers, and VMs. <br>
Mitigation: Use a Viewer-role API key, limit access to trusted agents and users, and review generated queries before execution. <br>
Risk: API keys may be exposed through command-line arguments, environment handling, debug JSON, or persisted dashboard inventory files. <br>
Mitigation: Prefer environment or secret-store injection over command-line keys, avoid logging responses with sensitive fields, and review or remove debug JSON and memory-bank inventory writes before use. <br>
Risk: The helper script uses curl with certificate verification disabled, which weakens HTTPS protection for API-key requests. <br>
Mitigation: Enable TLS certificate verification for trusted certificates, or explicitly accept self-signed-certificate risk only on controlled local networks. <br>


## Reference(s): <br>
- [Unraid API Complete Reference Guide](artifact/references/api-reference.md) <br>
- [Unraid API Endpoints Reference](artifact/references/endpoints.md) <br>
- [Unraid API Quick Reference](artifact/references/quick-reference.md) <br>
- [Unraid API Troubleshooting Guide](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell and GraphQL examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON API response interpretation and monitoring report text.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
