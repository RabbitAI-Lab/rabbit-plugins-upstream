## Description:

Secure database credential management using MGC Blackbox 1.4.10. Supports MySQL, PostgreSQL, SQLite, MariaDB and other databases. Credentials are stored encrypted; local scripts retrieve them via HTTP API at runtime, while AI agents never touch plaintext.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this documentation skill to design database access workflows where agents can request database operations without receiving plaintext credentials. It focuses on MGC Blackbox patterns for encrypted credential storage, blackbox script execution, credential rotation, and multi-node script sealing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may use the documented pattern to run arbitrary SQL against production databases without sufficient boundaries.

Mitigation: Use narrowly scoped database accounts and require explicit user approval for migrations, destructive SQL, or production database operations.

Risk: Database result files and script logs may expose sensitive data even when credentials are hidden from the agent.

Mitigation: Limit result contents, avoid logging credentials or sensitive rows, and review result files before sharing or retaining them.

Risk: Stored or sealed scripts can execute with local database credentials on a target node.

Mitigation: Review scripts before deployment, keep credentials local to each node, and verify credential references before calling blackbox execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/mgc-database-security)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown documentation with inline Python examples, shell commands, MCP tool call patterns, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; outputs implementation guidance and templates rather than directly executing database operations.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
