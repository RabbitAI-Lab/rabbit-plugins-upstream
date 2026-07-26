## Description: <br>
Query Veeam Backup & Replication and Veeam ONE via MCP server running in Docker. Provides intelligent backup monitoring, job analysis, capacity planning, and infrastructure health checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jgm2025](https://clawhub.ai/user/jgm2025) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, backup administrators, and infrastructure operators use this skill to query Veeam Backup & Replication and Veeam ONE through natural language or helper scripts for backup status, job analysis, repository capacity, alerts, and health checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an external Veeam MCP Docker image. <br>
Mitigation: Install only when the external image source is trusted and review the MCP tools exposed before using interactive mode. <br>
Risk: The credentials file can contain powerful backup-system credentials. <br>
Mitigation: Use a least-privilege service account and restrict ~/.veeam-mcp-creds.json to the local user. <br>
Risk: Example shell commands can place passwords in command history or process environments. <br>
Mitigation: Avoid entering passwords directly in example commands and prefer loading secrets from a protected credentials file. <br>
Risk: The scripts enable self-signed certificate acceptance. <br>
Mitigation: Prefer validated TLS certificates for Veeam endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jgm2025/skills/veeam-mcp) <br>
- [Model Context Protocol](https://modelcontextprotocol.io/) <br>
- [Veeam Intelligence Documentation](https://helpcenter.veeam.com/) <br>
- [OpenClaw documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Veeam query answers, setup steps, MCP tool listings, connection test results, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
