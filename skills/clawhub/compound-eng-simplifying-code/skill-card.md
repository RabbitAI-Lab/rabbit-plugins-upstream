## Description:

Simplifies, polishes, and declutters code without changing behavior when developers ask for cleanup, refactoring, dead-code removal, or readability improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to make conservative code simplification edits while preserving behavior, public interfaces, side effects, and domain intent. It also guides verification of tests, type checks, and scope boundaries after changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Code simplification edits can accidentally remove guards, retries, compatibility paths, or internal renames that still matter.

Mitigation: Review diffs carefully, especially deletions, and require tests or type checks that cover the changed paths before accepting edits.

Risk: Behavior parity can be hard to prove when tests are missing, scope is ambiguous, or code is intentionally complex for domain reasons.

Mitigation: Stop for human confirmation when behavior cannot be verified, when public APIs would change, or when complexity appears intentional.

## Reference(s):

- [Simplification patterns](artifact/references/simplification-patterns.md)
- [Orchestrated simplification](artifact/references/orchestrated-simplification.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with direct workspace edits, code diffs, and inline shell commands when verification is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior-preserving edits with verification notes and residual-risk reporting.]

## Skill Version(s):

4.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
