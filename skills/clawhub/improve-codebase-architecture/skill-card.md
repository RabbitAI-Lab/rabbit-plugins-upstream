## Description:

Surfaces architectural friction in a codebase and proposes evidence-backed deepening opportunities that improve testability and maintainability without writing production code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill for architecture-review passes that identify shallow modules, apply the deletion test, and decide which refactoring candidates deserve deeper interface design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads relevant project files and uses sub-agents during architecture review.

Mitigation: Use it only in repositories where that level of project inspection is acceptable.

Risk: The skill can make limited documentation edits, such as CONTEXT.md glossary updates, during follow-up discussion.

Mitigation: Review generated documentation changes like any other repository change before keeping them.

## Reference(s):

- [Language](artifact/LANGUAGE.md)
- [Interface Design](artifact/INTERFACE-DESIGN.md)
- [Deepening](artifact/DEEPENING.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown narrative with numbered candidate lists and optional repository documentation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not write production code; may update CONTEXT.md glossary entries or offer ADR documentation when the user accepts that workflow.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
