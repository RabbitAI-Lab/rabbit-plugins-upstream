## Description: <br>
Connect to test-environment MySQL databases for troubleshooting, data verification, schema inspection, and controlled validation queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[extraskittles](https://clawhub.ai/user/extraskittles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect test or development MySQL data, validate code behavior, troubleshoot environment issues, and perform explicitly approved low-risk test-data corrections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Database credentials, hostnames, or sensitive row values could be exposed in prompts, logs, generated files, or final summaries. <br>
Mitigation: Use least-privilege non-production credentials, keep TEST_MYSQL_* values out of generated artifacts, and redact passwords, tokens, personal data, payment data, and secrets in responses. <br>
Risk: Write SQL or broad destructive statements could modify the wrong data or schema in a test database. <br>
Mitigation: Prefer read-only queries, require explicit confirmation for writes, state the target environment and expected row count, use narrow predicates and transactions where possible, and prepare a rollback plan before execution. <br>
Risk: The skill could be pointed at a production database by mistake. <br>
Mitigation: Do not configure TEST_MYSQL_* variables or project settings for production databases, and confirm the target is a test or development environment before running queries. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown summaries with SQL snippets, shell commands, and optional table, JSON, or CSV query output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TEST_MYSQL_* environment variables by default and rejects non-read SQL unless explicitly allowed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
