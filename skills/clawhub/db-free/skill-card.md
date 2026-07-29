## Description: <br>
Provides basic database design and operations guidance for identifying and avoiding common connection, transaction, query performance, and data integrity pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database operators use this skill to identify basic database risks and choose safer patterns for connection pools, transactions, query design, and integrity constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Database guidance may include SQL or operational commands that could change production data or schema if applied without review. <br>
Mitigation: Confirm the target database, backup state, and data or schema impact before allowing an agent to execute suggested commands. <br>
Risk: The skill includes API key configuration guidance, which can lead to accidental credential exposure if copied into logs or version control. <br>
Mitigation: Use environment variables or a secrets manager, and do not commit credentials or paste them into shared transcripts. <br>
Risk: Broad database troubleshooting advice can be incomplete for advanced operations such as schema changes, backup recovery, replication, and scaling. <br>
Mitigation: Use the skill for basic triage and require expert review for production schema changes, recovery procedures, replication changes, and large-scale database planning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/db-free) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with SQL, Python, shell, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May suggest database commands or SQL changes that require human review before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
