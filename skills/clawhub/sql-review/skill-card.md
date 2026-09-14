## Description:

Pre-commit SQL code review for uncommitted database changes, focused on production-impacting SQL antipatterns such as broken TRY/CATCH handling, swallowed errors, missing table indexes, unsafe dynamic SQL, unscoped writes, and environment-specific references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill before committing SQL changes to review diffs for incident-prone patterns and receive severity-ranked findings with file and line citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects local SQL diffs and may read nearby SQL context to judge findings.

Mitigation: Run it only in repositories where the agent is allowed to inspect SQL files and review findings before sharing them outside the development team.

Risk: SQL fixes can affect production data or deployment behavior if applied without review.

Mitigation: Use the skill's report-first workflow and require explicit user approval before making any SQL edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/sql-review)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown findings report with file:line citations and suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports BLOCKER, WARN, and INFO findings and waits for explicit user approval before making SQL edits.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
