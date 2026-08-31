## Description:

Helps agents turn ideas, existing systems, changes, PRDs, prototypes, and acceptance work into traceable requirement artifacts with validation gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Product managers, designers, engineers, testers, and coding agents use this skill to clarify requirements, produce PRDs and prototypes, manage review baselines, analyze changes, build traceability, and prepare acceptance evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has a broad trigger surface for requirements, PRD, prototype, review, and acceptance tasks.

Mitigation: Configure the host to invoke it for those task families rather than every ambiguous conversation.

Risk: Local validation helpers may execute in the user's workspace.

Mitigation: Run Python and Node validation commands only in trusted workspaces after reviewing the release contents.

Risk: Static gates can be mistaken for proof of business correctness, real implementation behavior, legal compliance, or customer acceptance.

Mitigation: Keep the generated evidence boundary visible and require domain, implementation, browser, or customer evidence before making stronger claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [Lifecycle stages](references/stages.md)
- [Specification workflow](references/specify.md)
- [Prototype workflow](references/prototype.md)
- [Review workspace](references/review-workspace.md)
- [Change and acceptance workflow](references/change-acceptance.md)
- [Context management](references/context.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, YAML/JSON, HTML prototypes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs use stable IDs, traceability links, GAP/unknown markers, and explicit evidence boundaries.]

## Skill Version(s):

5.4.8 (source: evidence release and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
