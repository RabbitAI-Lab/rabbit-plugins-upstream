## Description:

Helps developers simplify and refactor existing code while preserving behavior and public APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkxzhou](https://clawhub.ai/user/linkxzhou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to make existing code easier to read and maintain without changing behavior or public interfaces. It supports edits to scoped code and read-only simplification assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refactoring local source code may unintentionally change behavior or public APIs.

Mitigation: Review the diff, preserve existing contracts, and run the project's available tests and checks before accepting changes.

Risk: Bundled evaluation harnesses execute code and may be unsafe to run on untrusted inputs.

Mitigation: Do not run the evaluation harnesses on untrusted code unless they are isolated in a sandbox.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/linkxzhou/skills/simplify-code-all)
- [Behavior traps](references/behavior-traps.md)
- [Simplification assessments](references/assessment.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with rewritten code or diffs and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope, skipped changes, and checks actually performed.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
