## Description:

Stores software-engineering knowledge such as personas, requirements, costs, architecture, runtime logic, and decisions in a local semantic graph so agents can retrieve precise context when fixing bugs, adding features, or refactoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[littlelollipop](https://clawhub.ai/user/littlelollipop)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to build and query a project-specific semantic graph across personas, requirements, architecture, modules, runtime logic, and historical decisions. It is intended to reduce context overload by retrieving only task-relevant traceability context before bug fixes, feature work, and refactoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on local lobster-memory and axolotl components, including in_neighbors support, so an incomplete dependency setup can prevent graph initialization or tracing.

Mitigation: Verify the lobster-memory and axolotl installation before use, including the documented import check for in_neighbors support.

Risk: The workflow stores user-confirmed project knowledge in a local graph, which can include sensitive requirements, design decisions, and project context.

Mitigation: Keep SE_SEMANTIC_DIR in an appropriate local project directory, review what is recorded, and avoid storing secrets or unnecessary full-text source content.

Risk: Incorrect semantic edge direction can make trace results misleading or incomplete.

Mitigation: Follow the documented problem-domain to implementation-domain edge direction and review graph updates during project milestones.

## Reference(s):

- [Server-resolved source repository](https://github.com/LittleLollipop/se-semantic-graph)
- [ClawHub skill page](https://clawhub.ai/littlelollipop/skills/se-semantic-graph)
- [lobster-memory dependency](https://github.com/LittleLollipop/lobster-memory.git)
- [Node templates](templates/node-templates.md)
- [Onboarding dialogue template](templates/onboarding-dialogue.md)
- [Requirement dimensions template](templates/requirement-dimensions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured graph-entry templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or querying of local project graph files through the bundled CLI.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
