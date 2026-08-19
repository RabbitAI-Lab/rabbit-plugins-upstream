## Description:

Pre-commit SQL review skill that inspects uncommitted SQL diffs for production incident patterns and reports BLOCKER, WARN, and INFO findings with cited evidence and fix recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill before committing SQL changes to identify risky database antipatterns in new SQL files and changed SQL hunks. It returns scoped review findings and user-directed fix recommendations rather than editing SQL automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects local SQL diffs and may quote changed SQL lines in its report.

Mitigation: Use it only in workspaces where the agent is allowed to inspect SQL changes, and review generated reports before sharing them outside the intended audience.

Risk: The review is heuristic and may produce false positives or miss context outside the scoped diff.

Mitigation: Treat findings as pre-commit guidance and verify blockers or warnings with the database owner before applying fixes.

Risk: SQL edits can affect production data or deployment behavior.

Mitigation: Follow the skill's approval gate: report findings first, then wait for explicit user approval before making any SQL change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/sql-review)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown review report with cited SQL snippets and fix recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are categorized as BLOCKER, WARN, or INFO and include file:line citations when issues are found.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
