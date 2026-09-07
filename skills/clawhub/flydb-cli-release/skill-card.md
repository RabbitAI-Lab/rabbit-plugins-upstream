## Description:

Helps agents use and troubleshoot Flydb CLI release packages, including installation, migration dry runs and execution, local Web workbench use, JSON and Plan output, MCP calls, JDBC driver setup, and Flydb error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to install or locate a Flydb CLI release, validate configuration, inspect and dry-run migration plans, execute authorized database migrations, use local Web or MCP entry points, and recover from common Flydb errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation or execution of Flydb and JDBC code that may be unpinned or untrusted.

Mitigation: Use trusted Flydb releases and JDBC drivers, prefer a preinstalled CLI or reviewed ZIP with known checksum or signature, pre-provision approved driver JARs, and set driver downloads to offline or never when possible.

Risk: Migration, baseline, repair, undo, and clean operations can modify or destroy database state.

Mitigation: Run validation and dry-run planning first, review the target and planned changes, use least-privileged credentials, and require explicit target-scoped authorization before production writes or clean/repair/undo actions.

Risk: Database credentials and JDBC URLs may appear in commands, configuration, logs, or reports.

Mitigation: Use environment variables or password files, redact JDBC URLs and credentials in outputs, and avoid placing secrets in command history, version control, SQL, or final reports.

Risk: MCP write tools can execute database-changing commands when write tools are enabled by the host.

Mitigation: Keep default MCP usage to read-only and planning tools unless writes are explicitly approved, use absolute working and config paths, and pre-provision drivers because MCP database tools should not download drivers during execution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zzxcoding/skills/flydb-cli-release)
- [Release package reference](references/release-package.md)
- [CLI command reference](references/commands.md)
- [Configuration reference](references/configuration.md)
- [Error code reference](references/errors.md)
- [JDBC driver reference](references/drivers.md)
- [JSON output reference](references/json-output.md)
- [Plan Artifact reference](references/plan-artifact.md)
- [MCP tools reference](references/mcp-tools.md)
- [Local Web workbench reference](references/web.md)
- [Local Web API reference](references/web-api.md)
- [JDBC integration reference](references/jdbc-integration.md)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run plans, redacted database targets, exit codes, status summaries, and remediation steps; should not expose passwords or raw secrets.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
