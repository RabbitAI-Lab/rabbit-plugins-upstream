## Description: <br>
Manage Neon serverless Postgres databases by creating projects, branches, databases, and running queries for agent workflows that need persistent storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawbot-ved](https://clawhub.ai/user/clawbot-ved) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to provision and manage Neon serverless Postgres projects, branches, databases, roles, connection strings, and SQL workflows from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Neon API keys and database connection strings that can expose database access if logged, shared, or stored insecurely. <br>
Mitigation: Use limited-scope credentials where possible, avoid including secrets in prompts or logs, and rotate any credential that may have been exposed. <br>
Risk: The skill includes delete, reset, schema-change, and SQL execution commands that can remove or alter projects, branches, databases, and data. <br>
Mitigation: Confirm project, branch, database, and role identifiers before execution, prefer disposable branches for experiments, and review destructive commands before running them. <br>


## Reference(s): <br>
- [Neon](https://neon.tech) <br>
- [Neon Console](https://console.neon.tech) <br>
- [Neon API Docs](https://api-docs.neon.tech) <br>
- [Neon CLI Reference](https://neon.tech/docs/reference/neon-cli) <br>
- [neonctl GitHub Repository](https://github.com/neondatabase/neonctl) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, SQL examples, environment variables, and CLI output format guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires neonctl, Neon authentication, and psql for SQL execution examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
