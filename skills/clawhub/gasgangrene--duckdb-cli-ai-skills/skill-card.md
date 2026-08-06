## Description: <br>
DuckDB CLI specialist for SQL analysis, data processing, and file conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data analysts, and engineers use this skill to ask an agent for DuckDB CLI guidance, SQL examples, file conversion commands, output formatting options, and safe database inspection workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DuckDB examples may create, insert, export, or overwrite data when run against important files or databases. <br>
Mitigation: Review paths and SQL intent before execution, use read-only mode for existing databases when appropriate, and keep backups before running write operations. <br>
Risk: Output redirection, COPY TO, .output, and ~/.duckdbrc examples can write files or change local CLI behavior. <br>
Mitigation: Confirm destination paths and configuration changes explicitly before running generated commands. <br>


## Reference(s): <br>
- [DuckDB CLI Overview](https://duckdb.org/docs/stable/clients/cli/overview) <br>
- [DuckDB CLI Arguments](https://duckdb.org/docs/stable/clients/cli/arguments) <br>
- [DuckDB Dot Commands](https://duckdb.org/docs/stable/clients/cli/dot_commands) <br>
- [DuckDB Output Formats](https://duckdb.org/docs/stable/clients/cli/output_formats) <br>
- [DuckDB CLI Safe Mode](https://duckdb.org/docs/stable/clients/cli/safe_mode) <br>
- [ClawHub Skill Page](https://clawhub.ai/gasgangrene/skills/duckdb-cli-ai-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with SQL and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include DuckDB CLI commands, SQL snippets, output format choices, and file conversion examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
