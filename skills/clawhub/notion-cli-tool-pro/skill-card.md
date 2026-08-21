## Description:

Notion命令行(专业版) guides agents through enterprise Notion CLI workflows for multi-workspace setup, schema management, batch operations, file handling, custom output, and audit logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to configure and operate a Notion CLI for multi-workspace administration, bulk database updates, exports, template output, and audited automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to modify, delete, export, sync, or schedule Notion data through CLI commands.

Mitigation: Use least-privilege Notion integrations, require dry runs for batch, schema, and delete operations, and review planned changes before execution.

Risk: Notion tokens, webhook keys, database credentials, and license keys may be exposed if provided inline or stored in plain text.

Mitigation: Keep secrets in environment variables or managed secret stores, avoid inline credentials, and rotate Notion integrations regularly.

Risk: Exec-enabled use depends on the installed Notion CLI package and the commands an agent is allowed to run.

Mitigation: Confirm the npm package source and version, define a command allowlist, and limit exec permissions to the required Notion CLI operations.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with bash, YAML, JSON, and Jinja2 examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command sequences that modify, delete, export, sync, or schedule Notion data.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
