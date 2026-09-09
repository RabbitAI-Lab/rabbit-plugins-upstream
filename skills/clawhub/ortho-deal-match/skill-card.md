## Description:

Ortho Deal Match helps agents operate a local, two-sided orthopedic sourcing workflow that scores buyer demands against seller capabilities and reveals contact details only after both sides confirm interest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and business operators use this skill to publish orthopedic buyer demands and seller capabilities, run five-dimension matching, manage introductions, and maintain local audit records for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages business and contact data in local SQLite and JSONL files, while its CLI role and consent controls are operational safeguards rather than strong authentication.

Mitigation: Restrict who can run the scripts, avoid shared workstations for sensitive records, and review blocklist, close, whoami, and reveal behavior before using it with real counterparties.

Risk: Runtime directories can contain contact records, audit history, database backups, and Python cache files after local use.

Mitigation: Exclude data/, registry/, audit/ including archive/, scripts/__pycache__/, .bak-* files, and *.pyc files from release packages.

## Reference(s):

- [Workflow Reference](references/WORKFLOW.md)
- [ClawHub Release Page](https://clawhub.ai/zhaoxinghua09-cell/skills/ortho-deal-match)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and local file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can create or update local SQLite, JSONL, and audit-log files when its commands are executed.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
