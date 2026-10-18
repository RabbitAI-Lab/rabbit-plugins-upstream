## Description:

Helps developers simplify and refactor existing code while preserving behavior and public APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkxzhou](https://clawhub.ai/user/linkxzhou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to make existing code clearer through scoped, behavior-preserving refactors or to assess possible simplifications without editing files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: In-place refactoring can introduce unintended changes to code behavior or public APIs.

Mitigation: Work from a clean working tree, compare the diff, and run relevant tests before accepting changes.

Risk: Broad cleanup requests can result in edits outside the intended area.

Mitigation: Specify the files or functions to change and review the reported scope.

## Reference(s):

- [Simplify Code release on ClawHub](https://clawhub.ai/linkxzhou/skills/simplify-code-all)
- [Simplification rules](references/rules.md)
- [Behavior traps](references/behavior-traps.md)
- [Read-only assessment guidance](references/assessment.md)
- [Source references](references/sources.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Code changes or Markdown assessment and verification summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope, checks run, and proposed changes requiring approval.]

## Skill Version(s):

1.1.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
