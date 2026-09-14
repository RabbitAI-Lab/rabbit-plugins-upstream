## Description:

Simplifies, polishes, and declutters code without changing behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to make disciplined, behavior-preserving simplification changes, including cleanup, refactoring, dead-code removal, and readability improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simplification edits could change behavior while appearing to only improve readability.

Mitigation: Review diffs for preserved interfaces, side effects, error behavior, and domain intent, then run the relevant tests and type checks.

Risk: Removing guards or workarounds can expose external hazards that tests may not exercise.

Mitigation: Require evidence that the hazard precondition is handled before removing the guard; otherwise retain it and document the gap.

Risk: Internal renames and broad refactors can miss non-import references such as fixtures, configuration, scripts, and documentation.

Mitigation: Search for old identifiers across the workspace and account for every remaining occurrence before completion.

## Reference(s):

- [Orchestrated simplification](references/orchestrated-simplification.md)
- [Simplification patterns](references/simplification-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summary with code changes, verification notes, and optional shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior-preserving changes with scope, simplification, verification, and residual-risk reporting]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
